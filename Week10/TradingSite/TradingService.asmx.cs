using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Security.Cryptography;
using System.Web.Script.Serialization;
using System.Web.Script.Services;
using System.Web.Services;
using System.Linq;

namespace TradingSite
{
    /// <summary>
    /// Summary description for TradingService
    /// </summary>
    [WebService(Namespace = "http://tempuri.org/")]
    [WebServiceBinding(ConformsTo = WsiProfiles.BasicProfile1_1)]
    [ToolboxItem(false)]
    // To allow this Web Service to be called from script, using ASP.NET AJAX, uncomment the following line. 
    [ScriptService]
    public class TradingService : WebService
    {
        List<StockQuote> _stockQuotes = new List<StockQuote>
                              {
                                  new StockQuote {CompanyCode = "ABC", Price = 100.50},
                                  new StockQuote {CompanyCode = "DEF", Price = 100.50},
                                  new StockQuote {CompanyCode = "PQR", Price = 100.50},
                                  new StockQuote {CompanyCode = "XYZ", Price = 100.50},
                              };

        [WebMethod]
        public string GetStockQuotes()
        {
            var data = new byte[]{100};
            _stockQuotes.ForEach(s =>
                                 {   new RNGCryptoServiceProvider().GetBytes(data);
                                     s.Price = Convert.ToDouble(data[0]);
                                 });
            var js = new JavaScriptSerializer();
            return js.Serialize(_stockQuotes);
        }
    }
}
