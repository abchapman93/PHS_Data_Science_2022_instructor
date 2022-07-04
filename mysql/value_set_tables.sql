CREATE TABLE PHS.value_set (
value_set_id MEDIUMINT NOT NULL AUTO_INCREMENT,
value_set_name VARCHAR(25) NOT NULL,
code_type VARCHAR(25) NOT NULL,
PRIMARY KEY (value_set_id)
);

CREATE TABLE PHS.value_set_value (
value_set_value_id MEDIUMINT NOT NULL AUTO_INCREMENT,
value_set_id MEDIUMINT NOT NULL,
code_value varchar(25) NOT NULL,
PRIMARY KEY (value_set_value_id)
);