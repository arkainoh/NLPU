using Newtonsoft.Json.Linq;
using System.IO;
using System.Net;
using System.Windows.Forms;

// dependency: Newtonsoft.Json

private string server_host;
private string server_port;

private string prefix = "http://" + server_host + ":" + server_port;

private void testPOST(string url) {
  string responseText = string.Empty;
  HttpWebRequest request = (HttpWebRequest)WebRequest.Create(url);
  request.Method = "POST";
  request.Timeout = 3 * 1000;
  using (HttpWebResponse resp = (HttpWebResponse)request.GetResponse())
  {
    HttpStatusCode status = resp.StatusCode;
    MessageBox.Show(status.ToString());

    Stream respStream = resp.GetResponseStream();
    using (StreamReader sr = new StreamReader(respStream))
    {
        responseText = sr.ReadToEnd();
    }
  }
  MessageBox.Show(responseText.ToString());
}

private void testGET(string url) {
  string responseText = string.Empty;
  HttpWebRequest request = (HttpWebRequest)WebRequest.Create(url);
  request.Method = "GET";
  request.Timeout = 3 * 1000;
  using (HttpWebResponse resp = (HttpWebResponse)request.GetResponse())
  {
    HttpStatusCode status = resp.StatusCode;
    MessageBox.Show(status.ToString());

    Stream respStream = resp.GetResponseStream();
    using (StreamReader sr = new StreamReader(respStream))
    {
        responseText = sr.ReadToEnd();
    }
  }
  MessageBox.Show(responseText.ToString());
  ParseJSON(responseText.ToString());
}

private void ParseJSON(string json)
{
  MessageBox.Show(json);
  JObject obj = JObject.Parse(json);

  foreach (var i in obj)
  {
      MessageBox.Show(i.Key + ": " + i.Value);
  }
}