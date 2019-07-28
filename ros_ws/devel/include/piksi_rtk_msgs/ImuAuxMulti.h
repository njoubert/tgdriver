// Generated by gencpp from file piksi_rtk_msgs/ImuAuxMulti.msg
// DO NOT EDIT!


#ifndef PIKSI_RTK_MSGS_MESSAGE_IMUAUXMULTI_H
#define PIKSI_RTK_MSGS_MESSAGE_IMUAUXMULTI_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>

#include <std_msgs/Header.h>

namespace piksi_rtk_msgs
{
template <class ContainerAllocator>
struct ImuAuxMulti_
{
  typedef ImuAuxMulti_<ContainerAllocator> Type;

  ImuAuxMulti_()
    : header()
    , imu_type(0)
    , temp(0)
    , imu_conf(0)  {
    }
  ImuAuxMulti_(const ContainerAllocator& _alloc)
    : header(_alloc)
    , imu_type(0)
    , temp(0)
    , imu_conf(0)  {
  (void)_alloc;
    }



   typedef  ::std_msgs::Header_<ContainerAllocator>  _header_type;
  _header_type header;

   typedef uint8_t _imu_type_type;
  _imu_type_type imu_type;

   typedef int16_t _temp_type;
  _temp_type temp;

   typedef uint8_t _imu_conf_type;
  _imu_conf_type imu_conf;





  typedef boost::shared_ptr< ::piksi_rtk_msgs::ImuAuxMulti_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::piksi_rtk_msgs::ImuAuxMulti_<ContainerAllocator> const> ConstPtr;

}; // struct ImuAuxMulti_

typedef ::piksi_rtk_msgs::ImuAuxMulti_<std::allocator<void> > ImuAuxMulti;

typedef boost::shared_ptr< ::piksi_rtk_msgs::ImuAuxMulti > ImuAuxMultiPtr;
typedef boost::shared_ptr< ::piksi_rtk_msgs::ImuAuxMulti const> ImuAuxMultiConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::piksi_rtk_msgs::ImuAuxMulti_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::piksi_rtk_msgs::ImuAuxMulti_<ContainerAllocator> >::stream(s, "", v);
return s;
}

} // namespace piksi_rtk_msgs

namespace ros
{
namespace message_traits
{



// BOOLTRAITS {'IsFixedSize': False, 'IsMessage': True, 'HasHeader': True}
// {'sensor_msgs': ['/opt/ros/melodic/share/sensor_msgs/cmake/../msg'], 'geometry_msgs': ['/opt/ros/melodic/share/geometry_msgs/cmake/../msg'], 'std_msgs': ['/opt/ros/melodic/share/std_msgs/cmake/../msg'], 'piksi_rtk_msgs': ['/home/gecko/Code/tgdriver/ros_ws/src/ethz_piksi_ros/piksi_rtk_msgs/msg']}

// !!!!!!!!!!! ['__class__', '__delattr__', '__dict__', '__doc__', '__eq__', '__format__', '__getattribute__', '__hash__', '__init__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_parsed_fields', 'constants', 'fields', 'full_name', 'has_header', 'header_present', 'names', 'package', 'parsed_fields', 'short_name', 'text', 'types']




template <class ContainerAllocator>
struct IsFixedSize< ::piksi_rtk_msgs::ImuAuxMulti_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::piksi_rtk_msgs::ImuAuxMulti_<ContainerAllocator> const>
  : FalseType
  { };

template <class ContainerAllocator>
struct IsMessage< ::piksi_rtk_msgs::ImuAuxMulti_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::piksi_rtk_msgs::ImuAuxMulti_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::piksi_rtk_msgs::ImuAuxMulti_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::piksi_rtk_msgs::ImuAuxMulti_<ContainerAllocator> const>
  : TrueType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::piksi_rtk_msgs::ImuAuxMulti_<ContainerAllocator> >
{
  static const char* value()
  {
    return "1d0e477b2db08e26ff9772a2136dfba7";
  }

  static const char* value(const ::piksi_rtk_msgs::ImuAuxMulti_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x1d0e477b2db08e26ULL;
  static const uint64_t static_value2 = 0xff9772a2136dfba7ULL;
};

template<class ContainerAllocator>
struct DataType< ::piksi_rtk_msgs::ImuAuxMulti_<ContainerAllocator> >
{
  static const char* value()
  {
    return "piksi_rtk_msgs/ImuAuxMulti";
  }

  static const char* value(const ::piksi_rtk_msgs::ImuAuxMulti_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::piksi_rtk_msgs::ImuAuxMulti_<ContainerAllocator> >
{
  static const char* value()
  {
    return "# Auxiliary data specific to a particular IMU. The 'imu type' field will always be consistent but the rest of\n"
"# the payload is device specific and depends on the value of 'imu type'.\n"
"\n"
"Header header\n"
"\n"
"uint8 imu_type  # IMU type.\n"
"int16 temp      # Raw IMU temperature.\n"
"uint8 imu_conf  # IMU configuration.\n"
"\n"
"================================================================================\n"
"MSG: std_msgs/Header\n"
"# Standard metadata for higher-level stamped data types.\n"
"# This is generally used to communicate timestamped data \n"
"# in a particular coordinate frame.\n"
"# \n"
"# sequence ID: consecutively increasing ID \n"
"uint32 seq\n"
"#Two-integer timestamp that is expressed as:\n"
"# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')\n"
"# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')\n"
"# time-handling sugar is provided by the client library\n"
"time stamp\n"
"#Frame this data is associated with\n"
"string frame_id\n"
;
  }

  static const char* value(const ::piksi_rtk_msgs::ImuAuxMulti_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::piksi_rtk_msgs::ImuAuxMulti_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.header);
      stream.next(m.imu_type);
      stream.next(m.temp);
      stream.next(m.imu_conf);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct ImuAuxMulti_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::piksi_rtk_msgs::ImuAuxMulti_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::piksi_rtk_msgs::ImuAuxMulti_<ContainerAllocator>& v)
  {
    s << indent << "header: ";
    s << std::endl;
    Printer< ::std_msgs::Header_<ContainerAllocator> >::stream(s, indent + "  ", v.header);
    s << indent << "imu_type: ";
    Printer<uint8_t>::stream(s, indent + "  ", v.imu_type);
    s << indent << "temp: ";
    Printer<int16_t>::stream(s, indent + "  ", v.temp);
    s << indent << "imu_conf: ";
    Printer<uint8_t>::stream(s, indent + "  ", v.imu_conf);
  }
};

} // namespace message_operations
} // namespace ros

#endif // PIKSI_RTK_MSGS_MESSAGE_IMUAUXMULTI_H
