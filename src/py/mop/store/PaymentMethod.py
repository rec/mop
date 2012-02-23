"""
package mop.store;

import "mop/store/PhoneNumber.proto";
import "mop/store/PostalAddress.proto";

option java_outer_classname = "PaymentMethodProto";

// A PaymentMethod is any way of accepting money from an Account.

message PaymentMethod {
  enum Type {
    NONE = 0;
    PAYPAL = 1;
    VISA = 2;
    MASTERCHARGE = 3;
    AMERICAN_EXPRESS = 4;
    DISCOVER = 5;
    EFTPOS = 6;
  };
  optional Type type = 1;

  optional string account_name = 2;
  optional string account_number = 3;
  optional PostalAddress billing_address = 4;
  optional PhoneNumber billing_phone_number = 5;
};
"""