USE subscribersdb;
ALTER TABLE subscribers ADD COLUMN IF NOT EXISTS status VARCHAR(20) DEFAULT 'active';
