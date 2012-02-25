"""package mop.store;

import "mop/store/PaymentMethod.proto";
import "mop/store/Person.proto";
import "mop/store/PhoneNumber.proto";
import "mop/store/PostalAddress.proto";
import "mop/store/Vehicle.proto";

option java_outer_classname = "AccountProto";

// An Account is some entity (a person, more than one person or a company) who
// can participate in Auctions.

message Account {
  // An immutable user id, probably the Google user ID (equivalent to a gmail
  // account).
  optional string account_id = 1;

  // The Person or Persons who own this account.
  repeated Person person = 2;

  // Any Vehicles that will be either parking or giving up parking space in
  // Auctions.
  repeated Vehicle vehicle = 3;

  // Any methods for giving or receiving money.
  repeated PaymentMethod payment_method = 4;

  optional PhoneNumber phone_number = 5;
  optional PostalAddress postal_address = 6;
};
"""