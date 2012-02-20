package mop.store;

import "mop/store/PhoneNumber.proto";
import "mop/store/PostalAddress.proto";

// A Person describes a "natural person" who will be taking one side or another
// of a Parking Transaction.
//
// A Person only exists as part of an Account, so we don't need to have a unique
// index for them.

option java_outer_classname = "PersonProto";

message Person {
  optional string prefix = 1;  // Mr.
  repeated string name = 2;  // John Wellington Wells
  optional string suffix = 3;  // Esq.

  optional string drivers_license = 4;
  optional PostalAddress drivers_license_issuer = 5;
};