# Is Source 2 Out Yet?

## Requirements

In order to install all the necessary dependencies, run `pip install -r requirements.txt` in the workspace folder after cloning the repository.

## Twitter Setup

[Create an app](https://developer.twitter.com/en/portal/projects-and-apps) on Twitter and generate the required credentials for your automated account (consumer keys & auth tokens).


## Configuration

Create a `.env` file in the workspace folder and fill in the credentials:

- `CONSUMER_KEY`
- `CONSUMER_SECRET`
- `ACCESS_KEY`
- `ACCESS_SECRET`

## Customisation

Make sure to specify the following data in `app.py`:

- Time of the day to schedule
- Desired timezone ([list of tz database](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones#List))
- Text of the tweet

## License

MIT