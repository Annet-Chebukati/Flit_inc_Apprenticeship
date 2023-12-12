CREATE TABLE hotel."Reservation"
(
    hotel character varying,
    is_canceled integer,
    lead_time integer,
    arrival_date_year integer,
    arrival_date_month character varying,
    arrival_date_week_number integer,
    arrival_date_day_of_month integer,
    stays_in_weekend_nights integer,
    stays_in_week_nights integer,
    adults integer,
    children character varying,
    babies integer,
    meal character varying,
    country character varying,
    market_segment character varying,
    distribution_channel character varying,
    is_repeated_guest integer,
    previous_cancellations integer,
    previous_bookings_not_canceled integer,
    reserved_room_type character varying,
    assigned_room_type character varying,
    booking_changes integer,
    deposit_type character varying,
    agent character varying,
    company character varying,
    days_in_waiting_list integer,
    customer_type character varying,
    adr numeric(6, 2),
    required_car_parking_spaces integer,
    total_of_special_requests integer,
    reservation_status character varying,
    reservation_status_date date
);

COPY hotel."Reservation" FROM 'C:/ANITA CHEBUKATI/FLIT/Hotel Reservation Analysis/Dataset_Hotel_Reservation_Analysis.csv' DELIMITER ',' CSV HEADER;

ALTER TABLE hotel."Reservation"
ADD COLUMN Reservation_id SERIAL PRIMARY KEY;

ALTER TABLE hotel."Reservation"
RENAME COLUMN adr TO average_daily_rate;


CREATE TABLE hotel."MarketSegment"
(
    market_segment character varying PRIMARY KEY,
    description character varying
);

INSERT INTO hotel."MarketSegment" (market_segment, description) VALUES
('Direct', 'Direct'),
('Corporate', 'Corporate'),
('Online TA', 'Online Travel Agents'),
('Offline TA/TO', 'Offline Travel Agents/Tour Operators'),
('Aviation', 'Aviation'),
('Complementary', 'Complementary'),
('Groups', 'Groups'),
('Undefined', 'Undefined');

CREATE TABLE hotel."DistributionChannel"
(
    distribution_channel character varying PRIMARY KEY,
    description character varying
);

INSERT INTO hotel."DistributionChannel" (distribution_channel, description) VALUES
('Corporate', 'Corporate'),
('Direct', 'Direct'),
('GDS', 'Global Distribution System'),
('TA/TO', 'Travel Agents/Tour Operators'),
('Undefined', 'Undefined');


CREATE TABLE hotel."Meal"
(
    meal character varying PRIMARY KEY,
    description character varying
);

INSERT INTO hotel."Meal" (meal, description) VALUES
('BB', 'Bed & Breakfast'),
('FB', 'Full board (breakfast, lunch and dinner)'),
('HB', 'Half board(breakfast and one other meal – usually dinner)'),
('SC', 'No meal package'),
('Undefined', 'Undefined');

ALTER TABLE hotel."Reservation"
ADD CONSTRAINT fk_market_segment
FOREIGN KEY (market_segment) REFERENCES hotel."MarketSegment" (market_segment);

ALTER TABLE hotel."Reservation"
ADD CONSTRAINT fk_distribution_channel
FOREIGN KEY (distribution_channel) REFERENCES hotel."DistributionChannel" (distribution_channel);

ALTER TABLE hotel."Reservation"
ADD CONSTRAINT fk_meal
FOREIGN KEY (meal) REFERENCES hotel."Meal" (meal);

COPY hotel."Reservation" TO 'C:/ANITA CHEBUKATI/FLIT/Hotel Reservation Analysis/Reservation.csv' DELIMITER ',' CSV HEADER;
COPY hotel."Meal" TO 'C:/ANITA CHEBUKATI/FLIT/Hotel Reservation Analysis/Meal.csv' DELIMITER ',' CSV HEADER;
COPY hotel."MarketSegment" TO 'C:/ANITA CHEBUKATI/FLIT/Hotel Reservation Analysis/MarketSegment.csv' DELIMITER ',' CSV HEADER;
COPY hotel."DistributionChannel" TO 'C:/ANITA CHEBUKATI/FLIT/Hotel Reservation Analysis/DistributionChannel.csv' DELIMITER ',' CSV HEADER;
