# Pokemon Go Twitter Status Bot
This is a simple script for running a Twitter bot to announce Pokemon Go service status changes. It's dependent upon querying a service leveraging the undocumented API for the service, so stability may vary.

The code has nothing built-in for re-running itself. It's designed to be run as a cron job/scheduled task.

## Dependencies
The code for querying the service status comes from a [gist linked to in Reddit for a user's i3 configuration](https://gist.github.com/donniebishop/a1cc00d9e1d6751a6f6ee64ca5d3e24f). This in turn requires Beautiful Soup for parsing the status out of a web page.

    pip install beautifulsoup4

The connection to Twitter is handled via [python-twitter](https://github.com/bear/python-twitter):

    pip install python-twitter

## Running.
Once it's configured properly, I recommend a manual run just to validate that things are as expected either via:

    python3 pokebot.py

Or you can make it executable:

    chmod +x pokebot.py
    ./pokebot.py

After that, I'd recommend setting up a cron job for it. I opt to run it every 5 minutes for my bot. This is inside of my user's crontable, accessible via `crontab -e`:

    */5 * * * * /path/to/file/pokebot.py

## Example.
My example of this script in action is at [IsPokemonAGo](https://twitter.com/IsPokeMonAGo).