```python
import pandas as pd

# Load the dataset (replace with your dataset path)
df = pd.read_csv('C:\\Users\\kesha\\Downloads\\urldata.csv\\urldata.csv')

# Inspect the dataset
df.sample(100)

```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Unnamed: 0</th>
      <th>url</th>
      <th>label</th>
      <th>result</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>443398</th>
      <td>443398</td>
      <td>https://sites.google.com/site/help410100020201...</td>
      <td>malicious</td>
      <td>1</td>
    </tr>
    <tr>
      <th>438435</th>
      <td>438435</td>
      <td>http://selectnext.com/penn/dbe/bidding/portal/...</td>
      <td>malicious</td>
      <td>1</td>
    </tr>
    <tr>
      <th>123771</th>
      <td>123771</td>
      <td>https://www.192.com/atoz/people/mcintosh/david/</td>
      <td>benign</td>
      <td>0</td>
    </tr>
    <tr>
      <th>58039</th>
      <td>58039</td>
      <td>https://www.icehockey.wikia.com/wiki/Jim_Montg...</td>
      <td>benign</td>
      <td>0</td>
    </tr>
    <tr>
      <th>131040</th>
      <td>131040</td>
      <td>https://www.allposters.com/-st/George-Stubbs-P...</td>
      <td>benign</td>
      <td>0</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>211441</th>
      <td>211441</td>
      <td>https://www.hockeydb.com/ihdb/stats/pdisplay.p...</td>
      <td>benign</td>
      <td>0</td>
    </tr>
    <tr>
      <th>440307</th>
      <td>440307</td>
      <td>https://sites.google.com/site/notificationhelp...</td>
      <td>malicious</td>
      <td>1</td>
    </tr>
    <tr>
      <th>364512</th>
      <td>364512</td>
      <td>http://larv.sunhut.net/images/gmail.com</td>
      <td>malicious</td>
      <td>1</td>
    </tr>
    <tr>
      <th>11165</th>
      <td>11165</td>
      <td>https://www.book.asiatravel.com/hotel.aspx?cn=...</td>
      <td>benign</td>
      <td>0</td>
    </tr>
    <tr>
      <th>439623</th>
      <td>439623</td>
      <td>http://eth2018.ethtoeth.com/</td>
      <td>malicious</td>
      <td>1</td>
    </tr>
  </tbody>
</table>
<p>100 rows × 4 columns</p>
</div>




```python

```
