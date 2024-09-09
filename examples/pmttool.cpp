#include <libintelpmt/libintelpmt.hpp>

#include <algorithm>
#include <iostream>
#include <thread>

void usage() {
  std::cout << "USAGE: pmttool command [options]..." << std::endl;
  std::cout << std::endl;
  std::cout << "Available commands:" << std::endl;
  std::cout << "\tlist " << std::endl;
  std::cout << "\tread [device] [counter_name]" << std::endl;
}

int main(int argc, char **argv) {
  if (argc == 1) {
    usage();
    return 0;
  }

  std::string command = argv[1];
  if (command == "list") {
    std::vector<intelpmt::Device> devices = intelpmt::get_pmt_devices();
    std::cout << "List: " << std::endl;

    for (auto &dev : devices) {
      std::cout << std::endl;
      std::cout << dev.get_uniqueid() << ":" << std::endl;
      for (auto &ev : dev.get_counter_names()) {
        std::cout << "\t" << ev.first << std::endl;
      }
    }

  } else if (command == "read") {
    if (argc != 4) {
      std::cout << "ERROR: \"read\" requires exactly two arguments: "
                << std::endl;
      std::cout << std::endl;
      usage();
      return 0;
    }

    std::string device_id = argv[2];
    std::string counter = argv[3];
    std::vector<intelpmt::Device> devices = intelpmt::get_pmt_devices();
    auto dev =
        std::find_if(devices.begin(), devices.end(), [&device_id](auto arg) {
          return arg.get_uniqueid() == device_id;
        });

    if (dev == devices.end()) {
      std::cout << "Unknown device: " << device_id << std::endl;
      return -1;
    }

    uint64_t counter_id = 0;
    try {
      counter_id = dev->get_counter_names().at(counter);
    } catch (std::out_of_range &e) {
      std::cout << "Unknown counter: " << counter << std::endl;
      return -1;
    }

    intelpmt::DeviceInstance instance = dev->open();

    std::cout << "Reading: " << counter
              << " every second until Ctrl+C is pressed" << std::endl;

    while (true) {
      std::visit([](auto arg) { std::cout << arg << std::endl; },
                 instance.read_counter(counter_id));
      std::this_thread::sleep_for(std::chrono::seconds(1));
    }
    return 0;

  }

  else {
    std::cout << "Unknown command: " << command << std::endl;
    return -1;
  }
}
