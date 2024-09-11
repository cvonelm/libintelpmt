#include <cassert>
#include <cstdint>
#include <cstring>
#include <filesystem>
#include <fstream>
#include <iostream>
#include <map>
#include <stdexcept>
#include <string>
#include <vector>

extern "C" {
#include <fcntl.h>
#include <sys/mman.h>
#include <unistd.h>
}

#pragma once

namespace intelpmt {


class DeviceInstance;
typedef double (*counter_read_f)(DeviceInstance &, std::vector<uint64_t>);

struct Sample {
  uint64_t offset; // in _bit_
  uint64_t size;   // in _bit_
};

struct Unit {
    std::string unit;
    std::string (*print_function)(double);
};

struct Counter {
  counter_read_f read_function;
  std::vector<uint64_t> sensors;
};
class Device {
public:
  Device(std::filesystem::path path) : path_(path) {}

  const std::map<std::string, uint64_t>& get_counter_names() const {
    return counter_names_;
  }

  const std::map<uint64_t, struct Sample>& get_samples() const {
    return samples_;
  }

  const std::map<uint64_t, struct Counter>& get_counters() const {
    return counters_;
  }

  const std::map<uint64_t, struct Unit>& get_units() const {
    return units_;
  }

  const std::filesystem::path get_path() const { return path_; }

  const uint64_t get_uniqueid() const { return uniqueid_; }

  DeviceInstance open();

protected:
  std::filesystem::path path_;
  uint64_t uniqueid_;
  std::map<uint64_t, struct Sample> samples_;
  std::map<std::string, uint64_t> counter_names_;
  std::map<uint64_t, struct Counter> counters_;
  std::map<uint64_t, struct Unit> units_;
};

class DeviceInstance {
public:
  DeviceInstance(Device &device) : device_(device) {
    fd_ = open((device_.get_path() / "telem").c_str(), O_RDONLY);

    if (fd_ == -1) {
      throw std::system_error(errno, std::system_category(), strerror(errno));
    }
    std::ifstream size_stream(device_.get_path() / "size");
    size_stream >> buf_size_;

    if (buf_size_ == 0) {
      throw std::runtime_error(std::string("Could not read ") +
                               (device_.get_path() / "size").string());
    }

    buf_ = (char *)mmap(NULL, buf_size_, PROT_READ, MAP_SHARED, fd_, 0);
    if (buf_ == MAP_FAILED) {
      throw std::system_error(errno, std::system_category(), strerror(errno));
    }
  }

  DeviceInstance(const DeviceInstance &other) = delete;
  DeviceInstance &operator=(const DeviceInstance &other) = delete;

  DeviceInstance(DeviceInstance &&other) : device_(other.device_) {
    buf_ = std::move(other.buf_);
    buf_size_ = std::move(other.buf_size_);
    std::swap(fd_, other.fd_);

    other.buf_ = nullptr;
  }

  DeviceInstance &operator=(DeviceInstance &&other) {
    if (buf_ != nullptr) {
      munmap(buf_, buf_size_);
      buf_ = nullptr;
    }

    if (fd_ != -1) {
      close(fd_);
      fd_ = -1;
    }

    device_ = other.device_;

    buf_ = std::move(other.buf_);
    buf_size_ = std::move(other.buf_size_);

    std::swap(fd_, other.fd_);

    other.buf_ = nullptr;

    return *this;
  }

  ~DeviceInstance() {
    if (buf_ != nullptr) {
      munmap(buf_, buf_size_);
      buf_ = nullptr;
    }

    if (fd_ != -1) {
      close(fd_);
      fd_ = -1;
    }
  }

  const Device &get_device() const { return device_; }

  uint64_t read_sample(uint64_t event) {
    uint64_t res;

    Sample sample = device_.get_samples().at(event);

    // Assumption of this code: Intel packs the values weirdly inside
    // 64-bit words, but values do _not_ span multiple words.
    // This assertion protects this assumption
    assert((sample.offset % 8) + sample.size <= 64);
    size_t byte_size = 0;

    if (sample.size % 8 == 0) {
      byte_size = sample.size / 8;
    } else {
      byte_size = (sample.size / 8) + 1;
    }

    memcpy(&res, buf_ + (sample.offset / 8), byte_size);

    res >>= sample.offset % 8;
    uint64_t mask = (1ULL << sample.size) - 1;
    return res & mask;
  }

  double read_counter(uint64_t counter_id) {
    const struct Counter counter = device_.get_counters().at(counter_id);
    return counter.read_function(*this, counter.sensors);
  }

private:
  Device &device_;
  char *buf_ = nullptr;
  size_t buf_size_ = 0;
  int fd_ = -1;
};
} // namespace intelpmt
