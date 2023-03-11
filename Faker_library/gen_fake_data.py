
from faker import Faker

fk = Faker()
'''
print(fk.last_name())
print(fk.first_name())
# Joseph
# Patrick

for i in range(1, 101, 1):
    print(i,',',fk.first_name(),',',fk.last_name())

# 1 , Cody , Hall
# 2 , Diane , Miller
# 3 , Calvin , Miller
# 4 , Joseph , Henderson
# 5 , Patricia , Martin
# 6 , Samantha , Booth
# 7 , Thomas , Young
# 8 , Jonathan , Leblanc
# 9 , Kristen , Browning
# 10 , Melissa , Lopez
# 11 , Donald , Mann
# 12 , Richard , Lane
# 13 , Pamela , Phelps
# 14 , Judy , Martinez
# 15 , Samantha , Howard
# 16 , Daniel , Miller
# 17 , Karla , Morgan
# 18 , James , Nolan
# 19 , Jeremy , Perez
# 20 , Andrew , Alvarez
# 21 , Benjamin , Santos
# 22 , Michelle , Cross
# 23 , Dale , Chavez
# 24 , Nicholas , Stewart
# 25 , Kenneth , Snyder
# 26 , Debra , Medina
# 27 , Tina , Moyer
# 28 , John , Pitts
# 29 , Samantha , Marks
# 30 , Kristen , Gonzales
# 31 , Lance , Walker
# 32 , Richard , Tran
# 33 , Lisa , Macdonald
# 34 , Matthew , Woods
# 35 , Kaitlyn , Bond
# 36 , Bonnie , Wolfe
# 37 , Alexa , Thompson
# 38 , William , Garza
# 39 , Mary , Rowland
# 40 , Bradley , Thompson
# 41 , Sylvia , Wilson
# 42 , Ronald , Cook
# 43 , Elizabeth , Browning
# 44 , Monica , Pratt
# 45 , Lucas , King
# 46 , Jessica , Thompson
# 47 , Tanya , Walton
# 48 , Cathy , Andrews
# 49 , Mary , Gibson
# 50 , William , Burke
# 51 , Haley , Lopez
# 52 , Lisa , Miller
# 53 , Lisa , Holder
# 54 , Dennis , Lester
# 55 , Janice , Cardenas
# 56 , Ashley , King
# 57 , Christina , Rodriguez
# 58 , Kristina , Morales
# 59 , Rodney , Tran
# 60 , Daniel , Nguyen
# 61 , Sean , Bennett
# 62 , Jacob , Houston
# 63 , Jacqueline , Young
# 64 , Evelyn , Lindsey
# 65 , Kathleen , Rodriguez
# 66 , Amanda , Goodman
# 67 , Christopher , Baldwin
# 68 , Gabrielle , Murray
# 69 , Charles , Simpson
# 70 , James , Miller
# 71 , Ashley , Parker
# 72 , Caitlin , Davis
# 73 , Danielle , Daniels
# 74 , Shirley , Rodriguez
# 75 , Chase , Hampton
# 76 , Janice , Paul
# 77 , Matthew , Mcgrath
# 78 , Candace , Vargas
# 79 , Scott , Sandoval
# 80 , Connie , Ruiz
# 81 , Paul , Cantu
# 82 , Mark , Brown
# 83 , Sean , Cole
# 84 , Jennifer , Vega
# 85 , Joel , Nash
# 86 , Mary , Mcgee
# 87 , Joseph , Smith
# 88 , Rachel , Scott
# 89 , Robert , Martin
# 90 , Roberto , Smith
# 91 , Benjamin , Smith
# 92 , Christopher , Stewart
# 93 , Mark , Moran
# 94 , Susan , Mcdaniel
# 95 , Rebecca , Diaz
# 96 , Cheyenne , Jenkins
# 97 , Carlos , Miller
# 98 , Kimberly , Hall
# 99 , Clinton , Owens
# 100 , Thomas , Grimes
'''

print(dir(fk))
list1 = ['aba', 'add_provider', 'address', 'administrative_unit', 'am_pm', 'android_platform_token',
         'ascii_company_email', 'ascii_email', 'ascii_free_email', 'ascii_safe_email',
         'bank_country', 'bban', 'binary', 'boolean', 'bothify', 'bs', 'building_number',
         'cache_pattern', 'catch_phrase', 'century', 'chrome', 'city', 'city_prefix',
         'city_suffix', 'color', 'color_name', 'company', 'company_email', 'company_suffix',
         'coordinate', 'country', 'country_calling_code', 'country_code', 'credit_card_expire',
         'credit_card_full', 'credit_card_number', 'credit_card_provider',
         'credit_card_security_code', 'cryptocurrency', 'cryptocurrency_code',
         'cryptocurrency_name', 'csv', 'currency', 'currency_code', 'currency_name',
         'currency_symbol', 'current_country', 'current_country_code', 'date', 'date_between',
         'date_between_dates', 'date_object', 'date_of_birth', 'date_this_century',
         'date_this_decade', 'date_this_month', 'date_this_year', 'date_time', 'date_time_ad',
         'date_time_between', 'date_time_between_dates', 'date_time_this_century',
         'date_time_this_decade', 'date_time_this_month', 'date_time_this_year', 'day_of_month',
         'day_of_week', 'del_arguments', 'dga', 'domain_name', 'domain_word', 'dsv', 'ean',
         'ean13', 'ean8', 'ein', 'email', 'enum', 'factories', 'file_extension', 'file_name',
         'file_path', 'firefox', 'first_name', 'first_name_female', 'first_name_male',
         'first_name_nonbinary', 'fixed_width', 'format', 'free_email', 'free_email_domain',
         'future_date', 'future_datetime', 'generator_attrs', 'get_arguments', 'get_formatter',
         'get_providers', 'hex_color', 'hexify', 'hostname', 'http_method', 'iana_id', 'iban',
         'image', 'image_url', 'internet_explorer', 'invalid_ssn', 'ios_platform_token', 'ipv4',
         'ipv4_network_class', 'ipv4_private', 'ipv4_public', 'ipv6', 'isbn10', 'isbn13',
         'iso8601', 'items', 'itin', 'job', 'json', 'language_code', 'language_name',
         'last_name', 'last_name_female', 'last_name_male', 'last_name_nonbinary', 'latitude',
         'latlng', 'lexify', 'license_plate', 'linux_platform_token', 'linux_processor',
         'local_latlng', 'locale', 'locales', 'localized_ean', 'localized_ean13',
         'localized_ean8', 'location_on_land', 'longitude', 'mac_address', 'mac_platform_token',
         'mac_processor', 'md5', 'military_apo', 'military_dpo', 'military_ship',
         'military_state', 'mime_type', 'month', 'month_name', 'msisdn', 'name', 'name_female',
         'name_male', 'name_nonbinary', 'nic_handle', 'nic_handles', 'null_boolean', 'numerify',
         'opera', 'paragraph', 'paragraphs', 'parse', 'password', 'past_date', 'past_datetime',
         'phone_number', 'port_number', 'postalcode', 'postalcode_in_state', 'postalcode_plus4',
         'postcode', 'postcode_in_state', 'prefix', 'prefix_female', 'prefix_male',
         'prefix_nonbinary', 'pricetag', 'profile', 'provider', 'providers', 'psv', 'pybool',
         'pydecimal', 'pydict', 'pyfloat', 'pyint', 'pyiterable', 'pylist', 'pyset', 'pystr',
         'pystr_format', 'pystruct', 'pytimezone', 'pytuple', 'random', 'random_choices',
         'random_digit', 'random_digit_not_null', 'random_digit_not_null_or_empty',
         'random_digit_or_empty', 'random_element', 'random_elements', 'random_int',
         'random_letter', 'random_letters', 'random_lowercase_letter', 'random_number',
         'random_sample', 'random_uppercase_letter', 'randomize_nb_elements', 'rgb_color',
         'rgb_css_color', 'ripe_id', 'safari', 'safe_color_name', 'safe_domain_name', 'safe_email',
         'safe_hex_color', 'secondary_address', 'seed', 'seed_instance', 'seed_locale', 'sentence',
         'sentences', 'set_arguments', 'set_formatter', 'sha1', 'sha256', 'simple_profile', 'slug',
         'ssn', 'state', 'state_abbr', 'street_address', 'street_name', 'street_suffix', 'suffix',
         'suffix_female', 'suffix_male', 'suffix_nonbinary', 'swift', 'swift11', 'swift8', 'tar',
         'text', 'texts', 'time', 'time_delta', 'time_object', 'time_series', 'timezone', 'tld',
         'tsv', 'unique', 'unix_device', 'unix_partition', 'unix_time', 'upc_a', 'upc_e', 'uri',
         'uri_extension', 'uri_page', 'uri_path', 'url', 'user_agent', 'user_name', 'uuid4',
         'weights', 'windows_platform_token', 'word', 'words', 'year', 'zip', 'zipcode',
         'zipcode_in_state', 'zipcode_plus4']
print(len(list1))