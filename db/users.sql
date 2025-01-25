-- SELECT current_database();

CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    uname TEXT NOT NULL,
    uage INT NOT NULL,
    uscore INT NOT NULL, -- шекели
    utg_username TEXT -- тэг в телеграме
);