g2 = new Dygraph( document.getElementById('graphdiv2'), 'DATE,Premium/Discount\n2021-11-16,0.0\n2021-11-17,-0.31533834952638395\n2021-11-18,-0.448100751574243\n2021-11-19,-0.5850588712951632\n2021-11-22,-0.4826845528784762\n2021-11-23,-0.4451080715905831\n2021-11-24,-0.08258914949449414\n2021-11-26,-0.11162813519680626\n2021-11-29,-0.15418213941008618\n2021-11-30,0.411762532483273\n2021-12-01,0.028272663202910664\n2021-12-02,-0.20240359358010274\n2021-12-03,-0.4011622687093319\n2021-12-06,0.02937600470016566\n2021-12-07,-0.039015350101800905\n2021-12-08,0.034399028733300696\n2021-12-09,0.04471453832239902\n2021-12-10,-0.05151774522650365\n2021-12-13,-0.18514826103056548\n2021-12-14,-0.20285714285714906\n2021-12-15,-0.2792862684251385\n2021-12-16,-0.09473679912124222\n2021-12-17,-0.0613602336597574\n2021-12-20,-0.12081278553875974\n2021-12-21,-0.032546450788939474\n2021-12-22,0.05749486652977254\n2021-12-23,0.14788415058784032\n2021-12-27,-0.16803967375712547\n2021-12-28,-0.16547861507127948\n2021-12-29,-0.09304240428159583\n2021-12-30,-0.05013870338025361\n2021-12-31,-0.02834013085748488\n2022-01-03,0.14946267550541847\n2022-01-04,-0.0879041434069805\n2022-01-05,0.0353973558998355\n2022-01-06,0.022605278949128227\n2022-01-07,-0.09211948511349544\n2022-01-10,-0.11550999099760872\n2022-01-11,0.08699310181459197\n2022-01-12,-0.008105731157215246\n2022-01-13,-0.10004982238118743\n2022-01-14,0.016601475506750063\n2022-01-18,-0.378542510121449\n2022-01-19,-0.1130098560738757\n2022-01-20,-0.10617296908873586\n2022-01-21,-0.3481947472565583\n2022-01-24,-0.22033045510615468\n2022-01-25,0.020288008569657734\n2022-01-26,-0.08482624824462937\n2022-01-27,-0.03255539503936866\n2022-01-28,-0.04395157187914167\n2022-01-31,-0.11252691741011622\n2022-02-01,-0.0028228879756952985\n2022-02-02,0.03508545526402784\n2022-02-03,-0.014183822337487939\n2022-02-04,-0.0890958793155705\n2022-02-07,-0.045234066098287506\n2022-02-08,-0.10972166196047128\n2022-02-09,-0.10013874645594667\n2022-02-10,-0.10397314430102833\n2022-02-11,-0.16258260245125555\n2022-02-14,-0.08732423975355008\n2022-02-15,-0.021306532663312172\n2022-02-16,-0.037639295424418684\n', { includeZero: true,     xlabel: 'Date',     xRangePad: 10,     ylabel: '<span style="position: absolute; transform: translate(-50%, -10px)">Premium/Discount</span>',     legend: 'always',     title: 'Historical Premium/Discount',     axisLabelFormatter: function (number) {                 if (typeof number === 'object') {                     return new Date(number).toLocaleDateString('en-us');                 }                 return parseFloat(number).toFixed(2) + '%';             },    valueFormatter: function (number) {                 var numDate = new Date(number);                 if (numDate > 1448327658) {                     return new Date(number).toLocaleDateString('en-us');                 }                 return parseFloat(number).toFixed(2) + '%';             }} );