-- V1__init.sql (MySQL-safe)

CREATE DATABASE IF NOT EXISTS subscribersdb;
USE subscribersdb;

-- If a partial table was created by a failed run, drop and recreate (no data yet)
DROP TABLE IF EXISTS subscribers;

CREATE TABLE subscribers (
  id INT AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(100) NOT NULL,
  email VARCHAR(255) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  -- add the unique constraint here (works across all MySQL 8)
  UNIQUE KEY ux_subscribers_email (email)
);