from config import CONFIG
import collection
import analyze

if __name__ == '__main__':

    resultfiles = dict()

    # collection
    resultfiles['tourspot_visitor'] = \
        collection.crawling_tourspot_visitor(CONFIG['district'], **CONFIG['common'])

    resultfiles['foreign_visitor'] = []
    for country in CONFIG['countries']:
        rf = collection.crawling_foreign_visitor(country, **CONFIG['common'])
        resultfiles['foreign_visitor'].append(rf)

    # analysis
    analyze.analysis_correlation(resultfiles)

    # vsualization
