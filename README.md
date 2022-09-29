# akahu2firefly
This project is a script that will export transactions from the akahu nz transactional data and accounts api's

https://developers.akahu.nz/docs/accessing-transactional-data

And then import those into a firefly iii budget manager instance

https://www.firefly-iii.org/

This is an early draft and has only been tested against a kiwibank feed

These api's are sensitive and will contain your personal financial data.

That data will also end up in the local sqlite file so take the appropriate measures to prevent that data ending up somewhere you dont want it.

# TODO
- A cli
- add updating of transactions that already exist based on conditional flags
- cli interface/script that lets you choose when to start importing from, if to update in place or only get new
- The records intermediate table is useful to have when debugging or investigating issues, but is not actually necessary for production usecases and is actually dangerous, as it contains financial data, make it so it is only populated and filled out when debug env vars are set
- Make the session table cleared at the end of the script runtime as well for the same reason, we only ever want the mapping information stored
- Add a validation mode that compares all existing mapped transactions to see if they're in firefly and removes them from the mapping table if not (allowing you to recreate them potentially)
