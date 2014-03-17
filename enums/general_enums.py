empties = [None, (), [], "", {}]

standard_buckets = [0,1,2,5,10,20]

days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

days_of_week = (
(1, 'Monday'),
(2, 'Tuesday'),
(3, 'Wednesday'),
(4, 'Thursday'),
(5, 'Friday'),
(6, 'Saturday'),
(7, 'Sunday'),
)

numerical_bool = (
(1, 'Yes'),
(0, 'No'),
)

data_requirement_types = (
('MD', 'Mandatory'),
('OC', 'Optional calculable'),
('ON', 'Optional non-calculable')
)

genders = (
('M', 'Male'),
('F', 'Female')
)

time_periods = (
('D', 'Days'),
('W', 'Weeks'),
('F', 'Fortnights'),
('M', 'Months'),
('Q', 'Quarters'),
('H', 'Halves'),
('Y', 'Years'),
)

time_period_conversions = {
				'D': 1.0,
			    'W': 7.0,
			    'F': 14.0,
			    'M': 365.242/12.0,
			    'Q': 365.242/4.0,
			    'H': 365.242/2.0,
			    'Y': 365.242
			}

marital_status = (
('S', 'Single'),
('M', 'Married'),
('W', 'Widowed'),
('D', 'Divorced'),
)

increase_or_decrease = (
('IN', 'Increase'),
('DE', 'Decrease'),
('NE', 'Neither'),
)

colours = (
('BL', 'Blue'),
('RD', 'Red'),
('GN', 'Green'),
('BN', 'Brown'),
('YL', 'Yellow'),
('WH', 'White'),
('BK', 'Black'),
('GY', 'Grey'),
('PP', 'Purple'),
('OG', 'Orange'),
('TL', 'Teal'),
)

ownership_types = (
('R', 'Rented'),
('B', 'Borrowed'),
('O', 'Owned')
)

BOOL_TRUES = ['true', '1', 't', 'y', 'yes', 'yeah', 'yup', 'certainly', 'uh-huh', True, 1]
BOOL_FALSES = ['false', '0', 'f', 'n', 'no', 'nope', 'nuh-uh', False, 0]

rounding = (
('UP', 'up'),
('DN', 'down'),
('EX', 'exact'),
)
