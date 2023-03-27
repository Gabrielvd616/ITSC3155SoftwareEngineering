# Migration plan for implementing new features
1. A new database schema would need to be created with a new playlist table/entity with a consumer_playlist many-to-many relationship table relating to consumers and a playlist_songs many-to-many relationship table relating to songs. Several other tables would also need additional columns as required for some new features.
2. A stored procedure mapping existing columns in the old database to columns in the new database schema would need to be developed with interpolation for data in new relationships.
3. The stored procedure would then need to be executed and the deep copies of the migrated data would need to be verified for correctness (could be done manually or with another stored procedure).
