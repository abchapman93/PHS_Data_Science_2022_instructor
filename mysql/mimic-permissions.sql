SELECT * FROM mysql.user


show grants for 'uu-phs';
revoke all privileges on *.* from 'uu-phs';
grant select on `db`.* to 'uu-phs';
flush privileges;