"""autogenerated by genpy from task_recorder2_srvs/StopRecordingRequest.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import task_recorder2_msgs.msg
import genpy

class StopRecordingRequest(genpy.Message):
  _md5sum = "8b474c64e40aca6a64757c639c1aee9f"
  _type = "task_recorder2_srvs/StopRecordingRequest"
  _has_header = False #flag to mark the presence of a Header object
  _full_text = """time crop_start_time
time crop_end_time
int32 num_samples
string[] message_names
bool stop_recording
task_recorder2_msgs/Description description

================================================================================
MSG: task_recorder2_msgs/Description
string SIDE_GRASP=side_grasp
string TOP_GRASP=top_grasp
string PLACING=placing
string RELEASING=releasing
string TURN_ON_DRILL=turn_on_drill
string DRILLING=drilling
string description
int32 id
int32 trial

"""
  __slots__ = ['crop_start_time','crop_end_time','num_samples','message_names','stop_recording','description']
  _slot_types = ['time','time','int32','string[]','bool','task_recorder2_msgs/Description']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       crop_start_time,crop_end_time,num_samples,message_names,stop_recording,description

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(StopRecordingRequest, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.crop_start_time is None:
        self.crop_start_time = genpy.Time()
      if self.crop_end_time is None:
        self.crop_end_time = genpy.Time()
      if self.num_samples is None:
        self.num_samples = 0
      if self.message_names is None:
        self.message_names = []
      if self.stop_recording is None:
        self.stop_recording = False
      if self.description is None:
        self.description = task_recorder2_msgs.msg.Description()
    else:
      self.crop_start_time = genpy.Time()
      self.crop_end_time = genpy.Time()
      self.num_samples = 0
      self.message_names = []
      self.stop_recording = False
      self.description = task_recorder2_msgs.msg.Description()

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      _x = self
      buff.write(_struct_4Ii.pack(_x.crop_start_time.secs, _x.crop_start_time.nsecs, _x.crop_end_time.secs, _x.crop_end_time.nsecs, _x.num_samples))
      length = len(self.message_names)
      buff.write(_struct_I.pack(length))
      for val1 in self.message_names:
        length = len(val1)
        if python3 or type(val1) == unicode:
          val1 = val1.encode('utf-8')
          length = len(val1)
        buff.write(struct.pack('<I%ss'%length, length, val1))
      buff.write(_struct_B.pack(self.stop_recording))
      _x = self.description.description
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_struct_2i.pack(_x.description.id, _x.description.trial))
    except struct.error as se: self._check_types(se)
    except TypeError as te: self._check_types(te)

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    try:
      if self.crop_start_time is None:
        self.crop_start_time = genpy.Time()
      if self.crop_end_time is None:
        self.crop_end_time = genpy.Time()
      if self.description is None:
        self.description = task_recorder2_msgs.msg.Description()
      end = 0
      _x = self
      start = end
      end += 20
      (_x.crop_start_time.secs, _x.crop_start_time.nsecs, _x.crop_end_time.secs, _x.crop_end_time.nsecs, _x.num_samples,) = _struct_4Ii.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.message_names = []
      for i in range(0, length):
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        start = end
        end += length
        if python3:
          val1 = str[start:end].decode('utf-8')
        else:
          val1 = str[start:end]
        self.message_names.append(val1)
      start = end
      end += 1
      (self.stop_recording,) = _struct_B.unpack(str[start:end])
      self.stop_recording = bool(self.stop_recording)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.description.description = str[start:end].decode('utf-8')
      else:
        self.description.description = str[start:end]
      _x = self
      start = end
      end += 8
      (_x.description.id, _x.description.trial,) = _struct_2i.unpack(str[start:end])
      self.crop_start_time.canon()
      self.crop_end_time.canon()
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      _x = self
      buff.write(_struct_4Ii.pack(_x.crop_start_time.secs, _x.crop_start_time.nsecs, _x.crop_end_time.secs, _x.crop_end_time.nsecs, _x.num_samples))
      length = len(self.message_names)
      buff.write(_struct_I.pack(length))
      for val1 in self.message_names:
        length = len(val1)
        if python3 or type(val1) == unicode:
          val1 = val1.encode('utf-8')
          length = len(val1)
        buff.write(struct.pack('<I%ss'%length, length, val1))
      buff.write(_struct_B.pack(self.stop_recording))
      _x = self.description.description
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_struct_2i.pack(_x.description.id, _x.description.trial))
    except struct.error as se: self._check_types(se)
    except TypeError as te: self._check_types(te)

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    try:
      if self.crop_start_time is None:
        self.crop_start_time = genpy.Time()
      if self.crop_end_time is None:
        self.crop_end_time = genpy.Time()
      if self.description is None:
        self.description = task_recorder2_msgs.msg.Description()
      end = 0
      _x = self
      start = end
      end += 20
      (_x.crop_start_time.secs, _x.crop_start_time.nsecs, _x.crop_end_time.secs, _x.crop_end_time.nsecs, _x.num_samples,) = _struct_4Ii.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.message_names = []
      for i in range(0, length):
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        start = end
        end += length
        if python3:
          val1 = str[start:end].decode('utf-8')
        else:
          val1 = str[start:end]
        self.message_names.append(val1)
      start = end
      end += 1
      (self.stop_recording,) = _struct_B.unpack(str[start:end])
      self.stop_recording = bool(self.stop_recording)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.description.description = str[start:end].decode('utf-8')
      else:
        self.description.description = str[start:end]
      _x = self
      start = end
      end += 8
      (_x.description.id, _x.description.trial,) = _struct_2i.unpack(str[start:end])
      self.crop_start_time.canon()
      self.crop_end_time.canon()
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
_struct_B = struct.Struct("<B")
_struct_4Ii = struct.Struct("<4Ii")
_struct_2i = struct.Struct("<2i")
"""autogenerated by genpy from task_recorder2_srvs/StopRecordingResponse.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import task_recorder2_msgs.msg
import std_msgs.msg

class StopRecordingResponse(genpy.Message):
  _md5sum = "7aa099c3f8e47ca0f1edca81fa0782f7"
  _type = "task_recorder2_srvs/StopRecordingResponse"
  _has_header = False #flag to mark the presence of a Header object
  _full_text = """task_recorder2_msgs/DataSample[] filtered_and_cropped_messages
task_recorder2_msgs/Description description
string info
int32 return_code
int32 SERVICE_CALL_FAILED = 0
int32 SERVICE_CALL_SUCCESSFUL = 1

================================================================================
MSG: task_recorder2_msgs/DataSample
Header header
float64[] data
string[] names
================================================================================
MSG: std_msgs/Header
# Standard metadata for higher-level stamped data types.
# This is generally used to communicate timestamped data 
# in a particular coordinate frame.
# 
# sequence ID: consecutively increasing ID 
uint32 seq
#Two-integer timestamp that is expressed as:
# * stamp.secs: seconds (stamp_secs) since epoch
# * stamp.nsecs: nanoseconds since stamp_secs
# time-handling sugar is provided by the client library
time stamp
#Frame this data is associated with
# 0: no frame
# 1: global frame
string frame_id

================================================================================
MSG: task_recorder2_msgs/Description
string SIDE_GRASP=side_grasp
string TOP_GRASP=top_grasp
string PLACING=placing
string RELEASING=releasing
string TURN_ON_DRILL=turn_on_drill
string DRILLING=drilling
string description
int32 id
int32 trial

"""
  # Pseudo-constants
  SERVICE_CALL_FAILED = 0
  SERVICE_CALL_SUCCESSFUL = 1

  __slots__ = ['filtered_and_cropped_messages','description','info','return_code']
  _slot_types = ['task_recorder2_msgs/DataSample[]','task_recorder2_msgs/Description','string','int32']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       filtered_and_cropped_messages,description,info,return_code

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(StopRecordingResponse, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.filtered_and_cropped_messages is None:
        self.filtered_and_cropped_messages = []
      if self.description is None:
        self.description = task_recorder2_msgs.msg.Description()
      if self.info is None:
        self.info = ''
      if self.return_code is None:
        self.return_code = 0
    else:
      self.filtered_and_cropped_messages = []
      self.description = task_recorder2_msgs.msg.Description()
      self.info = ''
      self.return_code = 0

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      length = len(self.filtered_and_cropped_messages)
      buff.write(_struct_I.pack(length))
      for val1 in self.filtered_and_cropped_messages:
        _v1 = val1.header
        buff.write(_struct_I.pack(_v1.seq))
        _v2 = _v1.stamp
        _x = _v2
        buff.write(_struct_2I.pack(_x.secs, _x.nsecs))
        _x = _v1.frame_id
        length = len(_x)
        if python3 or type(_x) == unicode:
          _x = _x.encode('utf-8')
          length = len(_x)
        buff.write(struct.pack('<I%ss'%length, length, _x))
        length = len(val1.data)
        buff.write(_struct_I.pack(length))
        pattern = '<%sd'%length
        buff.write(struct.pack(pattern, *val1.data))
        length = len(val1.names)
        buff.write(_struct_I.pack(length))
        for val2 in val1.names:
          length = len(val2)
          if python3 or type(val2) == unicode:
            val2 = val2.encode('utf-8')
            length = len(val2)
          buff.write(struct.pack('<I%ss'%length, length, val2))
      _x = self.description.description
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_struct_2i.pack(_x.description.id, _x.description.trial))
      _x = self.info
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      buff.write(_struct_i.pack(self.return_code))
    except struct.error as se: self._check_types(se)
    except TypeError as te: self._check_types(te)

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    try:
      if self.filtered_and_cropped_messages is None:
        self.filtered_and_cropped_messages = None
      if self.description is None:
        self.description = task_recorder2_msgs.msg.Description()
      end = 0
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.filtered_and_cropped_messages = []
      for i in range(0, length):
        val1 = task_recorder2_msgs.msg.DataSample()
        _v3 = val1.header
        start = end
        end += 4
        (_v3.seq,) = _struct_I.unpack(str[start:end])
        _v4 = _v3.stamp
        _x = _v4
        start = end
        end += 8
        (_x.secs, _x.nsecs,) = _struct_2I.unpack(str[start:end])
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        start = end
        end += length
        if python3:
          _v3.frame_id = str[start:end].decode('utf-8')
        else:
          _v3.frame_id = str[start:end]
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        pattern = '<%sd'%length
        start = end
        end += struct.calcsize(pattern)
        val1.data = struct.unpack(pattern, str[start:end])
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        val1.names = []
        for i in range(0, length):
          start = end
          end += 4
          (length,) = _struct_I.unpack(str[start:end])
          start = end
          end += length
          if python3:
            val2 = str[start:end].decode('utf-8')
          else:
            val2 = str[start:end]
          val1.names.append(val2)
        self.filtered_and_cropped_messages.append(val1)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.description.description = str[start:end].decode('utf-8')
      else:
        self.description.description = str[start:end]
      _x = self
      start = end
      end += 8
      (_x.description.id, _x.description.trial,) = _struct_2i.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.info = str[start:end].decode('utf-8')
      else:
        self.info = str[start:end]
      start = end
      end += 4
      (self.return_code,) = _struct_i.unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      length = len(self.filtered_and_cropped_messages)
      buff.write(_struct_I.pack(length))
      for val1 in self.filtered_and_cropped_messages:
        _v5 = val1.header
        buff.write(_struct_I.pack(_v5.seq))
        _v6 = _v5.stamp
        _x = _v6
        buff.write(_struct_2I.pack(_x.secs, _x.nsecs))
        _x = _v5.frame_id
        length = len(_x)
        if python3 or type(_x) == unicode:
          _x = _x.encode('utf-8')
          length = len(_x)
        buff.write(struct.pack('<I%ss'%length, length, _x))
        length = len(val1.data)
        buff.write(_struct_I.pack(length))
        pattern = '<%sd'%length
        buff.write(val1.data.tostring())
        length = len(val1.names)
        buff.write(_struct_I.pack(length))
        for val2 in val1.names:
          length = len(val2)
          if python3 or type(val2) == unicode:
            val2 = val2.encode('utf-8')
            length = len(val2)
          buff.write(struct.pack('<I%ss'%length, length, val2))
      _x = self.description.description
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_struct_2i.pack(_x.description.id, _x.description.trial))
      _x = self.info
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      buff.write(_struct_i.pack(self.return_code))
    except struct.error as se: self._check_types(se)
    except TypeError as te: self._check_types(te)

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    try:
      if self.filtered_and_cropped_messages is None:
        self.filtered_and_cropped_messages = None
      if self.description is None:
        self.description = task_recorder2_msgs.msg.Description()
      end = 0
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.filtered_and_cropped_messages = []
      for i in range(0, length):
        val1 = task_recorder2_msgs.msg.DataSample()
        _v7 = val1.header
        start = end
        end += 4
        (_v7.seq,) = _struct_I.unpack(str[start:end])
        _v8 = _v7.stamp
        _x = _v8
        start = end
        end += 8
        (_x.secs, _x.nsecs,) = _struct_2I.unpack(str[start:end])
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        start = end
        end += length
        if python3:
          _v7.frame_id = str[start:end].decode('utf-8')
        else:
          _v7.frame_id = str[start:end]
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        pattern = '<%sd'%length
        start = end
        end += struct.calcsize(pattern)
        val1.data = numpy.frombuffer(str[start:end], dtype=numpy.float64, count=length)
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        val1.names = []
        for i in range(0, length):
          start = end
          end += 4
          (length,) = _struct_I.unpack(str[start:end])
          start = end
          end += length
          if python3:
            val2 = str[start:end].decode('utf-8')
          else:
            val2 = str[start:end]
          val1.names.append(val2)
        self.filtered_and_cropped_messages.append(val1)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.description.description = str[start:end].decode('utf-8')
      else:
        self.description.description = str[start:end]
      _x = self
      start = end
      end += 8
      (_x.description.id, _x.description.trial,) = _struct_2i.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.info = str[start:end].decode('utf-8')
      else:
        self.info = str[start:end]
      start = end
      end += 4
      (self.return_code,) = _struct_i.unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
_struct_i = struct.Struct("<i")
_struct_2I = struct.Struct("<2I")
_struct_2i = struct.Struct("<2i")
class StopRecording(object):
  _type          = 'task_recorder2_srvs/StopRecording'
  _md5sum = 'f85fa88858d9abd1fe28a137b4bc1a4d'
  _request_class  = StopRecordingRequest
  _response_class = StopRecordingResponse
