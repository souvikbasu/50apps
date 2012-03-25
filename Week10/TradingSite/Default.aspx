<%@ Import Namespace="TradingSite" %>
<html>
<head>
<script type="text/javascript" src="Scripts/jquery-1.4.1.js"></script>
<script type="text/javascript">
    $(document).ready(function () {
        setInterval(getQuotes, 2000);
    });
    
    function getQuotes() {
        $.post("TradingService.asmx/GetStockQuotes", "",
        function (data) {
            var jsonText = data.childNodes[0].childNodes[0].data;
            var table = "<table>";
            JSON.parse(jsonText, function (key, value) {
                if (key === "CompanyCode") {
                    table += "<tr>";
                    table += "<td>" + value + "</td>";
                }
                else if (key === "Price") {
                    table += "<td>" + value + "</td>";
                    table += "</tr>";
                }
            });
            table += "</table>";
            $('#quotes').html(table);
        });
    };
</script>
</head>
<body>
    <h2>
        Stock Quotes
    </h2>
    <div id="quotes">
        Getting latest quotes from server ...
    </div>
    <div></div>
    </body>
</html>