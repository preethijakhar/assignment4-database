USE subscribersdb;
CREATE INDEX IF NOT EXISTS idx_subscribers_created_at ON subscribers(created_at);
