import cg,db

if __name__ == "__main__":
    print('--------------------------------------------------------')
    socials = {}
    tickers = cg.get_names()
    i = 0
    print('--------------------------------------------------------')
    for ticker in tickers:
        i+=1
        print('#{} getting info on: {}'.format(i, ticker))
        info =  cg.get_info(ticker)
        socials[ticker] = {}
        try:
            socials[ticker]['name'] = [ticker]
            socials[ticker]['price'] = info[1]
            socials[ticker]['market_cap']= info[2]
            socials[ticker]['volume'] = info[3]
            socials[ticker]['twitter_followers'] = info[0]['twitter_followers']
            socials[ticker]['tg_members'] = info[0]['telegram_channel_user_count']
            socials[ticker]['reddit_subscribers'] = info[0]['reddit_subscribers']
            socials[ticker]['active_reddit_users'] = info[0]['reddit_accounts_active_48h']
        except (ConnectionError, TypeError) as e:
            info =  cg.get_info(ticker)
            socials[ticker]['name'] = [ticker]
            socials[ticker]['price'] = info[1]
            socials[ticker]['market_cap']= info[2]
            socials[ticker]['volume'] = info[3]
            socials[ticker]['twitter_followers'] = info[0]['twitter_followers']
            socials[ticker]['tg_members'] = info[0]['telegram_channel_user_count']
            socials[ticker]['reddit_subscribers'] = info[0]['reddit_subscribers']
            socials[ticker]['active_reddit_users'] = info[0]['reddit_accounts_active_48h']

    print('--------------------------------------------------------')
    print('beginning data entry...')
    db.add_entry(socials)
    print('--------------------------------------------------   ------')    
    print('done!')
