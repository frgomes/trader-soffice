    __url = "http://biz.yahoo.com/p/"
    __xpathSectors      = '//table[2]/tr/td/table/tr/td[1]/a'
    __xpathIndustries   = '//table[2]/tr/td/table/tr/td[1]/a'
    __xpathCompanies    = '//table[2]/tr/td/table/tr[position()>4]'

    __labels = { 'symbol': 'Symbol',
                 'pricechange1d': 'Price Change 1d',
                 'marketcap': 'Market Cap',
                 'pe': 'Price/Equity',
                 'roe': 'Return on Equity',
                 'dividendyield': 'Dividend Yield',
                 'debttoequity': 'Debt/Equity',
                 'pricetobook': 'Price/Book',
                 'netprofitmargin': 'Net Profit Margin',
                 'pricetofreecashflow': 'Price to Free CashFlow', }


    def companies(self, url):
        '''
        Returns a generator which contains companies of a given industry.
        Every tuple is made of

            ``[ symbol,
                sector,
                industry,
                company,
                priceChange1d,
                marketCap,
                pe,
                roe,
                dividendYield,
                debtToEquity,
                priceToBook,
                netProfitMargin,
                priceToFreeCashFlow ]``

        >>> import etlsrc
        >>> loader = etlsrc.api.YahooProfileLoader()
        >>> companies = loader.companies('914conameu.html')
        >>> count = 0
        >>> for company in companies:
        ...  if count > 10:
        ...      break
        ...  count = count + 1
        ...  print('%(symbol)s %(company)s' % company)
        ACP.MI AcquePotabili
        AWR AmericanStates Water Company
        AWK AmericanWater Works Company,
        A2A.DE AquaAmerica Inc
        WTR AquaAmerica Inc.
        ARTNA ArtesianResources Corp.
        CDZI CadizInc.
        CWT CaliforniaWater Service Group
        BAUH78.SA CASAN
        0855.HK ChinaWater Affairs Group Ltd.
        CUBB.DE ChinaWater Affairs Group Ltd.

        '''
        # load HTML file
        url = self.__url + url
        content = self.request(url)
        if content is None: return
        from lxml import html
        rows = html.parse(content).xpath(self.__xpathCompanies)
        # process records
        if (rows is None):
            return
        else:
            for row in rows:
                cell = self.normalise(row.xpath("./td[1]/font")[0].text_content(), self.newlineFixings)
                (company, symbol) = self.parseNameAndSymbol(cell)
                # extract URL
                try:
                    text = row.xpath("./td/font/a[2]")[0].get('href')
                    parts = text.split('*')
                    parts = parts[1].split('&')
                    url = parts[0]
                except:
                    url = None
                # extract other pieces of information
                try:
                    priceChange1d       = self.parseFloat( row.xpath("./td[ 2]/font")[0].text_content() )
                    marketCap           = self.parseFloat( row.xpath("./td[ 3]/font")[0].text_content() )
                    pe                  = self.parseFloat( row.xpath("./td[ 4]/font")[0].text_content() )
                    roe                 = self.parseFloat( row.xpath("./td[ 5]/font")[0].text_content() )
                    dividendYield       = self.parseFloat( row.xpath("./td[ 6]/font")[0].text_content() )
                    debtToEquity        = self.parseFloat( row.xpath("./td[ 7]/font")[0].text_content() )
                    priceToBook         = self.parseFloat( row.xpath("./td[ 8]/font")[0].text_content() )
                    netProfitMargin     = self.parseFloat( row.xpath("./td[ 9]/font")[0].text_content() )
                    priceToFreeCashFlow = self.parseFloat( row.xpath("./td[10]/font")[0].text_content() )
                    yield { 'pricechange1d': priceChange1d,
                            'marketcap': marketCap,
                            'pe': pe,
                            'roe': roe,
                            'dividendyield': dividendYield,
                            'debttoequity': debtToEquity,
                            'pricetobook': priceToBook,
                            'netprofitmargin': netProfitMargin,
                            'pricetofreecashflow': priceToFreeCashFlow,
                            'symbol': symbol,
                            'url': url,
                            'sector': '',
                            'industry': '',
                            'company': company }
                except Exception as e:
                    msg = "%s;%s;%s;%s" % (symbol, company, url, e)
                    self.__logger.error(msg)
                    raise RuntimeError(msg)
            return
