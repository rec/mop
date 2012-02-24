"""package mop.store;

option java_outer_classname = "PostalAddressProto";

message PostalAddress {
  optional string intro = 1;  // c/o John Smith
  optional string unit_number = 2;  // Room 5
  optional string street_number = 3;  // 1600
  optional string street_name = 4;  // Pennsylvania Av NW
  optional string city = 5;  // Washington
  optional string district = 6;  // (rare in US)
  optional string state = 7;  // DC
  optional string postal_code = 8; // 20500
  optional string postal_subcode = 9;  // Zip+4, e.g.
  optional string country = 10;  // USA

  repeated string notes = 11;  // Won't be printed on envelopes...
};"""