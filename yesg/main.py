import calendar
import urllib.request
import json
import pandas as pd
import requests


# Downloads the numerical risk ratings of a company.
def get_esg_short(ticker):
    return __get_esg_data(ticker, False)


# Downloads the numerical risk ratings as well as all other available sustainability information about a company.
def get_esg_full(ticker):
    return __get_esg_data(ticker, True)


# Downloads historic ESG ratings and returns it as a dataframe
def get_historic_esg(ticker):
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) '
                             'Chrome/50.0.2661.102 Safari/537.36'}

    response = requests.get('https://query2.finance.yahoo.com/v1/finance/esgChart', params={"symbol": ticker},
                            headers=headers)

    try:
        df = pd.DataFrame(response.json()["esgChart"]["result"][0]["symbolSeries"])
        df["Date"] = pd.to_datetime(df["timestamp"], unit="s")

        df = df.rename(columns={"esgScore": "Total-Score", "environmentScore": "E-Score", "socialScore": "S-Score",
                                "governanceScore": "G-Score"})

        return df[['Date', 'Total-Score', 'E-Score', 'S-Score', 'G-Score']].set_index('Date')

    except:
        print('An error has occurred. The ticker symbol might be wrong or you might need to wait to continue.')


# Gets the actual information
def __get_esg_data(ticker, full):
    controversial_areas = ''

    with urllib.request.urlopen("https://query1.finance.yahoo.com/v10/finance/quoteSummary/" +
                                ticker + "?modules=esgScores") as url:
        data = json.loads(url.read().decode())

    try:
        totalScore = data["quoteSummary"]["result"][0]["esgScores"]["totalEsg"]["fmt"]
    except:
        totalScore = '-'

    try:
        EScore = data["quoteSummary"]["result"][0]["esgScores"]["environmentScore"]["fmt"]
    except:
        EScore = '-'

    try:
        SScore = data["quoteSummary"]["result"][0]["esgScores"]["socialScore"]["fmt"]
    except:
        SScore = '-'

    try:
        GScore = data["quoteSummary"]["result"][0]["esgScores"]["governanceScore"]["fmt"]
    except:
        GScore = '-'

    try:
        date = data["quoteSummary"]["result"][0]["esgScores"]["ratingYear"]
    except:
        date = '-'

    try:
        date = calendar.month_abbr[data["quoteSummary"]["result"][0]["esgScores"]["ratingMonth"]] + ' ' + str(date)
    except:
        date = '-'

    if not full:
        return pd.DataFrame({'Ticker': ticker,
                             'Total-Score': totalScore,
                             'E-Score': EScore,
                             'S-Score': SScore,
                             'G-Score': GScore,
                             'Last Rated': date}, index=[0])

    if full:

        try:
            highestControversy = data["quoteSummary"]["result"][0]["esgScores"]["highestControversy"]
        except:
            highestControversy = '-'

        try:
            peerCount = data["quoteSummary"]["result"][0]["esgScores"]["peerCount"]
        except:
            peerCount = '-'

        try:
            esgPerformance = data["quoteSummary"]["result"][0]["esgScores"]["esgPerformance"]
        except:
            esgPerformance = '-'

        try:
            peerGroup = data["quoteSummary"]["result"][0]["esgScores"]["peerGroup"]
        except:
            peerGroup = '-'

        try:
            relatedControversy = data["quoteSummary"]["result"][0]["esgScores"]["relatedControversy"]
            relatedControversy = ','.join(relatedControversy)
        except:
            relatedControversy = '-'

        try:
            peerEsgScorePerformance_min = \
                data["quoteSummary"]["result"][0]["esgScores"]["peerEsgScorePerformance"]["min"]
        except:
            peerEsgScorePerformance_min = '-'

        try:
            peerEsgScorePerformance_avg = \
                data["quoteSummary"]["result"][0]["esgScores"]["peerEsgScorePerformance"]["avg"]
        except:
            peerEsgScorePerformance_avg = '-'

        try:
            peerEsgScorePerformance_max = \
                data["quoteSummary"]["result"][0]["esgScores"]["peerEsgScorePerformance"]["max"]
        except:
            peerEsgScorePerformance_max = '-'

        try:
            peerGovernancePerformance_min = \
                data["quoteSummary"]["result"][0]["esgScores"]["peerGovernancePerformance"]["min"]
        except:
            peerGovernancePerformance_min = '-'

        try:
            peerGovernancePerformance_avg = \
                data["quoteSummary"]["result"][0]["esgScores"]["peerGovernancePerformance"]["avg"]
        except:
            peerGovernancePerformance_avg = '-'

        try:
            peerGovernancePerformance_max = \
                data["quoteSummary"]["result"][0]["esgScores"]["peerGovernancePerformance"]["max"]
        except:
            peerGovernancePerformance_max = '-'

        try:
            peerSocialPerformance_min = data["quoteSummary"]["result"][0]["esgScores"]["peerSocialPerformance"]["min"]
        except:
            peerSocialPerformance_min = '-'

        try:
            peerSocialPerformance_avg = data["quoteSummary"]["result"][0]["esgScores"]["peerSocialPerformance"]["avg"]
        except:
            peerSocialPerformance_avg = '-'

        try:
            peerSocialPerformance_max = data["quoteSummary"]["result"][0]["esgScores"]["peerSocialPerformance"]["max"]
        except:
            peerSocialPerformance_max = '-'

        try:
            peerEnvironmentPerformance_min = \
                data["quoteSummary"]["result"][0]["esgScores"]["peerEnvironmentPerformance"]["min"]
        except:
            peerEnvironmentPerformance_min = '-'

        try:
            peerEnvironmentPerformance_avg = \
                data["quoteSummary"]["result"][0]["esgScores"]["peerEnvironmentPerformance"]["avg"]
        except:
            peerEnvironmentPerformance_avg = '-'

        try:
            peerEnvironmentPerformance_max = \
                data["quoteSummary"]["result"][0]["esgScores"]["peerEnvironmentPerformance"]["max"]
        except:
            peerEnvironmentPerformance_max = '-'

        try:
            peerHighestControversyPerformance_min = \
                data["quoteSummary"]["result"][0]["esgScores"]["peerHighestControversyPerformance"]["min"]
        except:
            peerHighestControversyPerformance_min = '-'

        try:
            peerHighestControversyPerformance_avg = \
                data["quoteSummary"]["result"][0]["esgScores"]["peerHighestControversyPerformance"]["avg"]
        except:
            peerHighestControversyPerformance_avg = '-'

        try:
            peerHighestControversyPerformance_max = \
                data["quoteSummary"]["result"][0]["esgScores"]["peerHighestControversyPerformance"]["max"]
        except:
            peerHighestControversyPerformance_max = '-'

        try:
            totalPercentile = data["quoteSummary"]["result"][0]["esgScores"]["percentile"]["raw"]
        except:
            totalPercentile = '-'

        try:
            environmentPercentile = data["quoteSummary"]["result"][0]["esgScores"]["environmentPercentile"]
        except:
            environmentPercentile = '-'

        try:
            governancePercentile = data["quoteSummary"]["result"][0]["esgScores"]["governancePercentile"]
        except:
            governancePercentile = '-'

        try:
            socialPercentile = data["quoteSummary"]["result"][0]["esgScores"]["socialPercentile"]
        except:
            socialPercentile = '-'

        try:
            if data["quoteSummary"]["result"][0]["esgScores"]["adult"]:
                controversial_areas += 'Adult Entertainment, '
        except:
            pass

        try:
            if data["quoteSummary"]["result"][0]["esgScores"]["alcoholic"]:
                controversial_areas += 'Alcoholic Beverages, '
        except:
            pass

        try:
            if data["quoteSummary"]["result"][0]["esgScores"]["animalTesting"]:
                controversial_areas += 'Animal Testing, '
        except:
            pass

        try:
            if data["quoteSummary"]["result"][0]["esgScores"]["catholic"]:
                controversial_areas += 'Catholic Values, '
        except:
            pass

        try:
            if data["quoteSummary"]["result"][0]["esgScores"]["controversialWeapons"]:
                controversial_areas += 'Controversial Weapons, '
        except:
            pass

        try:
            if data["quoteSummary"]["result"][0]["esgScores"]["smallArms"]:
                controversial_areas += 'Small Arms, '
        except:
            pass

        try:
            if data["quoteSummary"]["result"][0]["esgScores"]["furLeather"]:
                controversial_areas += 'Fur and Specialty Leather, '
        except:
            pass

        try:
            if data["quoteSummary"]["result"][0]["esgScores"]["gambling"]:
                controversial_areas += 'Gambling, '
        except:
            pass

        try:
            if data["quoteSummary"]["result"][0]["esgScores"]["gmo"]:
                controversial_areas += 'GMO, '
        except:
            pass

        try:
            if data["quoteSummary"]["result"][0]["esgScores"]["militaryContract"]:
                controversial_areas += 'Military Contracting, '
        except:
            pass

        try:
            if data["quoteSummary"]["result"][0]["esgScores"]["nuclear"]:
                controversial_areas += 'Nuclear, '
        except:
            pass

        try:
            if data["quoteSummary"]["result"][0]["esgScores"]["pesticides"]:
                controversial_areas += 'Pesticides, '
        except:
            pass

        try:
            if data["quoteSummary"]["result"][0]["esgScores"]["palmOil"]:
                controversial_areas += 'Palm Oil, '
        except:
            pass

        try:
            if data["quoteSummary"]["result"][0]["esgScores"]["coal"]:
                controversial_areas += 'Thermal Coal, '
        except:
            pass

        try:
            if data["quoteSummary"]["result"][0]["esgScores"]["tobacco"]:
                controversial_areas += 'Tobacco Products, '
        except:
            pass

        if full:
            return pd.DataFrame({'Ticker': ticker,
                                 'Total-Score': totalScore,
                                 'E-Score': EScore,
                                 'S-Score': SScore,
                                 'G-Score': GScore,
                                 'Last Rated': date,
                                 'ESG Performance': esgPerformance,
                                 'peer Group': peerGroup,
                                 'Highest Controversy': highestControversy,
                                 'peer Count': peerCount,

                                 'total Percentile': totalPercentile,
                                 'environment Percentile': environmentPercentile,
                                 'social Percentile': socialPercentile,
                                 'governance Percentile': governancePercentile,
                                 'related Controversy': relatedControversy,
                                 'min peer ESG': peerEsgScorePerformance_min,
                                 'avg peer ESG': peerEsgScorePerformance_avg,
                                 'max peer ESG': peerEsgScorePerformance_max,
                                 'min peer Environment': peerEnvironmentPerformance_min,
                                 'avg peer Environment': peerEnvironmentPerformance_avg,
                                 'max peer Environment': peerEnvironmentPerformance_max,
                                 'min peer Social': peerSocialPerformance_min,
                                 'avg peer Social': peerSocialPerformance_avg,
                                 'max peer Social': peerSocialPerformance_max,
                                 'min peer Governance': peerGovernancePerformance_min,
                                 'avg peer Governance': peerGovernancePerformance_avg,
                                 'max peer Governance': peerGovernancePerformance_max,
                                 'min Highest Controversy': peerHighestControversyPerformance_min,
                                 'avg Highest Controversy': peerHighestControversyPerformance_avg,
                                 'max Highest Controversy': peerHighestControversyPerformance_max,
                                 'Controversial Business Areas': controversial_areas}, index=[0])
