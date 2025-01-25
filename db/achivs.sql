CREATE TABLE IF NOT EXISTS achivs (
    ach_id SERIAL PRIMARY KEY NOT NULL,
    name TEXT NOT NULL,
    date_was DATE NOT NULL,
    income INT NOT NULL
);

SELECT * FROM achivs;

-- CREATE TABLE IF NOT EXISTS user_achivs (
--     id SERIAL PRIMARY KEY NOT NULL,
--     uid INT REFERENCES users(id) ON DELETE CASCADE, -- юзер
--     achid INT 
-- );

-- DROP TABLE achivs;