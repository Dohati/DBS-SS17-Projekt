CREATE TABLE "tweet" (
	iD integer PRIMARY KEY, 
	handle text NOT NULL, 
	text text NOT NULL,
	retweet_count integer DEFAULT 0,
	favorite_count integer DEFAULT 0,
	time text NOT NULL
);

CREATE TABLE "hashtag"(
	iD integer PRIMARY KEY,
	name text NOT NULL UNIQUE
);

CREATE TABLE "enthält"(
	tweet_id integer REFERENCES tweet (iD),
	hashtag_id integer REFERENCES hashtag (iD)
);
