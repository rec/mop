"""import

class Vehicle(
  enum Type {
    NONE = 0;
    BICYCLE = 1;
    MOPED = 2;
    MOTORCYCLE = 3;
    SUBCOMPACT_CAR = 4;
    COMPACT_CAR = 5;
    MIDSIZE_CAR = 6;
    SEDAN_CAR = 7;
    STATIONWAGON_CAR = 8;
    LIGHT_VAN = 9;
    HEAVY_VAN = 10;
    MULTI_AXLE_TRUCK = 11;
  };
  optional Type type = 1;

  // This is normalized to meters, but presented in the Person's own units.
  optional float length = 2;
  optional uint32 axles = 3 [default = 2];

  optional string make = 4;
  optional string model = 5;
  optional uint32 year = 6;
  optional string description = 7;

  // We might legally have to request this in some places.
  optional string registration_number = 8;
};
"""