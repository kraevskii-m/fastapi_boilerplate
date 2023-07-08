BEGIN;

DROP TABLE IF EXISTS profile;
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

CREATE
    OR REPLACE FUNCTION update_timestamp()
    RETURNS TRIGGER AS
$$
BEGIN
    NEW.updated
        = now();
    RETURN NEW;
END;
$$
    LANGUAGE 'plpgsql';

CREATE TABLE profile
(
    id         UUID        DEFAULT uuid_generate_v4() PRIMARY KEY,
    first_name TEXT        DEFAULT NULL,
    last_name  TEXT        DEFAULT NULL,
    created    TIMESTAMPTZ DEFAULT now(),
    updated    TIMESTAMPTZ DEFAULT now(),
    password   TEXT        DEFAULT NULL,
    email      TEXT        DEFAULT NULL UNIQUE
);

CREATE TRIGGER update_my_table_timestamp
    BEFORE UPDATE
    ON profile
    FOR EACH ROW
EXECUTE FUNCTION update_timestamp();

COMMIT;
