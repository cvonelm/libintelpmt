#include <libintelpmt/device.hpp>

namespace intelpmt {

DeviceInstance Device::open() { return DeviceInstance(*this); }
} // namespace intelpmt
