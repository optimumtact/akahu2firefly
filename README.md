# akahu2firefly
This project is a script that will export transactions from the akahu nz transactional data and accounts api's

https://developers.akahu.nz/docs/accessing-transactional-data

And then import those into a firefly iii budget manager instance

https://www.firefly-iii.org/

This is an early draft and has only been tested against a kiwibank feed

These api's are sensitive and will contain your personal financial data.

That data will also end up in the local sqlite file so take the appropriate measures to prevent that data ending up somewhere you dont want it.