from mailsnake import MailSnake
import settings

ms_api = MailSnake(settings.API_KEY)
ms_export = MailSnake(settings.API_KEY, api='export')

def get_stats(campaigns):
    """
    Takes a list of campaigns and returns a stats dict whose keys are emails and whose values are dicts (with activity counts keyed to campaign times)
    """
    emails = []
    stats = {}

    for campaign in campaigns:
        campaign_time = campaign['send_time']
        campaign_activity = get_activity(campaign)

        if len(emails) == 0:
            emails = get_emails(campaign_activity)
            stats = {email: {} for email in emails}

        for subscriber in campaign_activity:
            email, activity = subscriber.popitem()

            if not stats.has_key(email):
                continue # Ignore people who are no longer subscribed

            if not stats[email].has_key(campaign_time):
                stats[email][campaign_time] = 0

            for item in activity:
                if item['action'] == 'open' or item['action'] == 'click':
                    stats[email][campaign_time] = stats[email][campaign_time] + 1

    return stats

# Returns list of email addresses
def get_emails(campaign_activity):
    """
    Returns a list of emails from a given campaign activity dict
    """
    return [d.keys()[0] for d in campaign_activity]

def get_activity(campaign):
    """
    Returns a dict with all activity for a given campaign
    """
    params = {'id': campaign['id'], 'include_empty': True}
    return ms_export.call("campaignSubscriberActivity", params=params)

def get_campaigns(from_name, limit=10):
    """
    Returns up to limit campaigns with 'from_name' from_name
    """
    params = {'filters': {'from_name': from_name}, 'limit': limit}
    return ms_api.call("campaigns", params=params)['data']


if __name__ == "__main__":
    campaigns = get_campaigns(settings.FROM_NAME, limit=settings.MAX_CAMPAIGNS)

    stats = get_stats(campaigns)

    campaign_times = [campaign['send_time'] for campaign in campaigns]
    headings = ["email"] + campaign_times

    # Print CSV of stats
    print ",".join(headings)
    for email, activity in stats.items():
        print ",".join([email] + [str(activity.get(time, 0)) for time in campaign_times])
