// Generated by gencpp from file piksi_rtk_msgs/ReceiverState_V2_3_15.msg
// DO NOT EDIT!


#ifndef PIKSI_RTK_MSGS_MESSAGE_RECEIVERSTATE_V2_3_15_H
#define PIKSI_RTK_MSGS_MESSAGE_RECEIVERSTATE_V2_3_15_H


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
struct ReceiverState_V2_3_15_
{
  typedef ReceiverState_V2_3_15_<ContainerAllocator> Type;

  ReceiverState_V2_3_15_()
    : header()
    , num_sat(0)
    , rtk_mode_fix(false)
    , sat()
    , cn0()
    , system_error(0)
    , io_error(0)
    , swift_nap_error(0)
    , external_antenna_present(0)
    , num_gps_sat(0)
    , cn0_gps()
    , num_sbas_sat(0)
    , cn0_sbas()
    , num_glonass_sat(0)
    , cn0_glonass()
    , fix_mode()  {
    }
  ReceiverState_V2_3_15_(const ContainerAllocator& _alloc)
    : header(_alloc)
    , num_sat(0)
    , rtk_mode_fix(false)
    , sat(_alloc)
    , cn0(_alloc)
    , system_error(0)
    , io_error(0)
    , swift_nap_error(0)
    , external_antenna_present(0)
    , num_gps_sat(0)
    , cn0_gps(_alloc)
    , num_sbas_sat(0)
    , cn0_sbas(_alloc)
    , num_glonass_sat(0)
    , cn0_glonass(_alloc)
    , fix_mode(_alloc)  {
  (void)_alloc;
    }



   typedef  ::std_msgs::Header_<ContainerAllocator>  _header_type;
  _header_type header;

   typedef uint8_t _num_sat_type;
  _num_sat_type num_sat;

   typedef uint8_t _rtk_mode_fix_type;
  _rtk_mode_fix_type rtk_mode_fix;

   typedef std::vector<uint8_t, typename ContainerAllocator::template rebind<uint8_t>::other >  _sat_type;
  _sat_type sat;

   typedef std::vector<uint8_t, typename ContainerAllocator::template rebind<uint8_t>::other >  _cn0_type;
  _cn0_type cn0;

   typedef uint8_t _system_error_type;
  _system_error_type system_error;

   typedef uint8_t _io_error_type;
  _io_error_type io_error;

   typedef uint8_t _swift_nap_error_type;
  _swift_nap_error_type swift_nap_error;

   typedef uint8_t _external_antenna_present_type;
  _external_antenna_present_type external_antenna_present;

   typedef uint8_t _num_gps_sat_type;
  _num_gps_sat_type num_gps_sat;

   typedef std::vector<uint8_t, typename ContainerAllocator::template rebind<uint8_t>::other >  _cn0_gps_type;
  _cn0_gps_type cn0_gps;

   typedef uint8_t _num_sbas_sat_type;
  _num_sbas_sat_type num_sbas_sat;

   typedef std::vector<uint8_t, typename ContainerAllocator::template rebind<uint8_t>::other >  _cn0_sbas_type;
  _cn0_sbas_type cn0_sbas;

   typedef uint8_t _num_glonass_sat_type;
  _num_glonass_sat_type num_glonass_sat;

   typedef std::vector<uint8_t, typename ContainerAllocator::template rebind<uint8_t>::other >  _cn0_glonass_type;
  _cn0_glonass_type cn0_glonass;

   typedef std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other >  _fix_mode_type;
  _fix_mode_type fix_mode;




  static const std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other >  STR_FIX_MODE_INVALID;
  static const std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other >  STR_FIX_MODE_SPP;
  static const std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other >  STR_FIX_MODE_DGNSS;
  static const std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other >  STR_FIX_MODE_FLOAT_RTK;
  static const std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other >  STR_FIX_MODE_FIXED_RTK;
  static const std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other >  STR_FIX_MODE_DEAD_RECKONING;
  static const std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other >  STR_FIX_MODE_SBAS;
  static const std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other >  STR_FIX_MODE_UNKNOWN;

  typedef boost::shared_ptr< ::piksi_rtk_msgs::ReceiverState_V2_3_15_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::piksi_rtk_msgs::ReceiverState_V2_3_15_<ContainerAllocator> const> ConstPtr;

}; // struct ReceiverState_V2_3_15_

typedef ::piksi_rtk_msgs::ReceiverState_V2_3_15_<std::allocator<void> > ReceiverState_V2_3_15;

typedef boost::shared_ptr< ::piksi_rtk_msgs::ReceiverState_V2_3_15 > ReceiverState_V2_3_15Ptr;
typedef boost::shared_ptr< ::piksi_rtk_msgs::ReceiverState_V2_3_15 const> ReceiverState_V2_3_15ConstPtr;

// constants requiring out of line definition

   
   template<typename ContainerAllocator> const std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other > 
      ReceiverState_V2_3_15_<ContainerAllocator>::STR_FIX_MODE_INVALID =
        
          "Invalid"
        
        ;
   

   
   template<typename ContainerAllocator> const std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other > 
      ReceiverState_V2_3_15_<ContainerAllocator>::STR_FIX_MODE_SPP =
        
          "SPP"
        
        ;
   

   
   template<typename ContainerAllocator> const std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other > 
      ReceiverState_V2_3_15_<ContainerAllocator>::STR_FIX_MODE_DGNSS =
        
          "DGNSS"
        
        ;
   

   
   template<typename ContainerAllocator> const std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other > 
      ReceiverState_V2_3_15_<ContainerAllocator>::STR_FIX_MODE_FLOAT_RTK =
        
          "FLOAT_RTK"
        
        ;
   

   
   template<typename ContainerAllocator> const std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other > 
      ReceiverState_V2_3_15_<ContainerAllocator>::STR_FIX_MODE_FIXED_RTK =
        
          "FIXED_RTK"
        
        ;
   

   
   template<typename ContainerAllocator> const std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other > 
      ReceiverState_V2_3_15_<ContainerAllocator>::STR_FIX_MODE_DEAD_RECKONING =
        
          "DEAD_RECKONING"
        
        ;
   

   
   template<typename ContainerAllocator> const std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other > 
      ReceiverState_V2_3_15_<ContainerAllocator>::STR_FIX_MODE_SBAS =
        
          "SBAS"
        
        ;
   

   
   template<typename ContainerAllocator> const std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other > 
      ReceiverState_V2_3_15_<ContainerAllocator>::STR_FIX_MODE_UNKNOWN =
        
          "Unknown"
        
        ;
   



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::piksi_rtk_msgs::ReceiverState_V2_3_15_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::piksi_rtk_msgs::ReceiverState_V2_3_15_<ContainerAllocator> >::stream(s, "", v);
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
struct IsFixedSize< ::piksi_rtk_msgs::ReceiverState_V2_3_15_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::piksi_rtk_msgs::ReceiverState_V2_3_15_<ContainerAllocator> const>
  : FalseType
  { };

template <class ContainerAllocator>
struct IsMessage< ::piksi_rtk_msgs::ReceiverState_V2_3_15_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::piksi_rtk_msgs::ReceiverState_V2_3_15_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::piksi_rtk_msgs::ReceiverState_V2_3_15_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::piksi_rtk_msgs::ReceiverState_V2_3_15_<ContainerAllocator> const>
  : TrueType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::piksi_rtk_msgs::ReceiverState_V2_3_15_<ContainerAllocator> >
{
  static const char* value()
  {
    return "88c8f10862fd18e3d9be4baddbd4a786";
  }

  static const char* value(const ::piksi_rtk_msgs::ReceiverState_V2_3_15_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x88c8f10862fd18e3ULL;
  static const uint64_t static_value2 = 0xd9be4baddbd4a786ULL;
};

template<class ContainerAllocator>
struct DataType< ::piksi_rtk_msgs::ReceiverState_V2_3_15_<ContainerAllocator> >
{
  static const char* value()
  {
    return "piksi_rtk_msgs/ReceiverState_V2_3_15";
  }

  static const char* value(const ::piksi_rtk_msgs::ReceiverState_V2_3_15_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::piksi_rtk_msgs::ReceiverState_V2_3_15_<ContainerAllocator> >
{
  static const char* value()
  {
    return "# Miscellaneous information form different SBP messages\n"
"\n"
"# Message definition based on libsbp v2.3.15\n"
"\n"
"\n"
"Header header\n"
"\n"
"uint8 num_sat                   # Number of satellites.\n"
"bool rtk_mode_fix 	            # 1 = Fixed, 0 = Float.\n"
"uint8[] sat                     # Constellation-specific satellite identifier.\n"
"uint8[] cn0                     # Carrier-to-Noise density. Zero implies invalid cn0 [dB Hz / 4].\n"
"uint8 system_error              # System Error Flag.\n"
"uint8 io_error                  # IO Error Flag.\n"
"uint8 swift_nap_error           # SwiftNAP Error Flag.\n"
"uint8 external_antenna_present  # External Antenna Present Flag.\n"
"uint8 num_gps_sat               # Number of GPS satellites.\n"
"uint8[] cn0_gps                 # Carrier-to-Noise density of GPS satellites. Zero implies invalid cn0 [dB Hz / 4].\n"
"uint8 num_sbas_sat              # Number of SBAS satellites.\n"
"uint8[] cn0_sbas                # Carrier-to-Noise density of SBAS satellites. Zero implies invalid cn0 [dB Hz / 4].\n"
"uint8 num_glonass_sat           # Number of GLONASS satellites.\n"
"uint8[] cn0_glonass             # Carrier-to-Noise density of GLONASS satellites. Zero implies invalid cn0 [dB Hz / 4].\n"
"string fix_mode                 # Invalid, Single Point Position (SPP), Differential GNSS (DGNSS), Float RTK, Fixed RTK.\n"
"\n"
"\n"
"# codes available in message \"TrackingState_V2_3_15.msg\"\n"
"\n"
"string STR_FIX_MODE_INVALID        = Invalid\n"
"string STR_FIX_MODE_SPP            = SPP\n"
"string STR_FIX_MODE_DGNSS          = DGNSS\n"
"string STR_FIX_MODE_FLOAT_RTK      = FLOAT_RTK\n"
"string STR_FIX_MODE_FIXED_RTK      = FIXED_RTK\n"
"string STR_FIX_MODE_DEAD_RECKONING = DEAD_RECKONING\n"
"string STR_FIX_MODE_SBAS           = SBAS\n"
"string STR_FIX_MODE_UNKNOWN        = Unknown\n"
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

  static const char* value(const ::piksi_rtk_msgs::ReceiverState_V2_3_15_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::piksi_rtk_msgs::ReceiverState_V2_3_15_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.header);
      stream.next(m.num_sat);
      stream.next(m.rtk_mode_fix);
      stream.next(m.sat);
      stream.next(m.cn0);
      stream.next(m.system_error);
      stream.next(m.io_error);
      stream.next(m.swift_nap_error);
      stream.next(m.external_antenna_present);
      stream.next(m.num_gps_sat);
      stream.next(m.cn0_gps);
      stream.next(m.num_sbas_sat);
      stream.next(m.cn0_sbas);
      stream.next(m.num_glonass_sat);
      stream.next(m.cn0_glonass);
      stream.next(m.fix_mode);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct ReceiverState_V2_3_15_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::piksi_rtk_msgs::ReceiverState_V2_3_15_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::piksi_rtk_msgs::ReceiverState_V2_3_15_<ContainerAllocator>& v)
  {
    s << indent << "header: ";
    s << std::endl;
    Printer< ::std_msgs::Header_<ContainerAllocator> >::stream(s, indent + "  ", v.header);
    s << indent << "num_sat: ";
    Printer<uint8_t>::stream(s, indent + "  ", v.num_sat);
    s << indent << "rtk_mode_fix: ";
    Printer<uint8_t>::stream(s, indent + "  ", v.rtk_mode_fix);
    s << indent << "sat[]" << std::endl;
    for (size_t i = 0; i < v.sat.size(); ++i)
    {
      s << indent << "  sat[" << i << "]: ";
      Printer<uint8_t>::stream(s, indent + "  ", v.sat[i]);
    }
    s << indent << "cn0[]" << std::endl;
    for (size_t i = 0; i < v.cn0.size(); ++i)
    {
      s << indent << "  cn0[" << i << "]: ";
      Printer<uint8_t>::stream(s, indent + "  ", v.cn0[i]);
    }
    s << indent << "system_error: ";
    Printer<uint8_t>::stream(s, indent + "  ", v.system_error);
    s << indent << "io_error: ";
    Printer<uint8_t>::stream(s, indent + "  ", v.io_error);
    s << indent << "swift_nap_error: ";
    Printer<uint8_t>::stream(s, indent + "  ", v.swift_nap_error);
    s << indent << "external_antenna_present: ";
    Printer<uint8_t>::stream(s, indent + "  ", v.external_antenna_present);
    s << indent << "num_gps_sat: ";
    Printer<uint8_t>::stream(s, indent + "  ", v.num_gps_sat);
    s << indent << "cn0_gps[]" << std::endl;
    for (size_t i = 0; i < v.cn0_gps.size(); ++i)
    {
      s << indent << "  cn0_gps[" << i << "]: ";
      Printer<uint8_t>::stream(s, indent + "  ", v.cn0_gps[i]);
    }
    s << indent << "num_sbas_sat: ";
    Printer<uint8_t>::stream(s, indent + "  ", v.num_sbas_sat);
    s << indent << "cn0_sbas[]" << std::endl;
    for (size_t i = 0; i < v.cn0_sbas.size(); ++i)
    {
      s << indent << "  cn0_sbas[" << i << "]: ";
      Printer<uint8_t>::stream(s, indent + "  ", v.cn0_sbas[i]);
    }
    s << indent << "num_glonass_sat: ";
    Printer<uint8_t>::stream(s, indent + "  ", v.num_glonass_sat);
    s << indent << "cn0_glonass[]" << std::endl;
    for (size_t i = 0; i < v.cn0_glonass.size(); ++i)
    {
      s << indent << "  cn0_glonass[" << i << "]: ";
      Printer<uint8_t>::stream(s, indent + "  ", v.cn0_glonass[i]);
    }
    s << indent << "fix_mode: ";
    Printer<std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other > >::stream(s, indent + "  ", v.fix_mode);
  }
};

} // namespace message_operations
} // namespace ros

#endif // PIKSI_RTK_MSGS_MESSAGE_RECEIVERSTATE_V2_3_15_H
