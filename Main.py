import cg,db

if __name__ == "__main__":

    socials = {}
    tickers = cg.get_names()


    for ticker in tickers:
        info =  cg.get_info(ticker)
        socials[ticker] = {}
        socials[ticker]['name'] = [ticker]
        socials[ticker]['price'] = info[1]
        socials[ticker]['twitter_followers'] = info[0]['twitter_followers']
        socials[ticker]['tg_members'] = info[0]['telegram_channel_user_count']
        socials[ticker]['reddit_subscribers'] = info[0]['reddit_subscribers']
        socials[ticker]['active_reddit_users'] = info[0]['reddit_accounts_active_48h']

    db.add_entry(socials)
    print('done!')