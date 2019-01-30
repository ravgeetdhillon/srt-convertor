# srt-convertor
A tool to convert Subtitles into Text format.

<h3>How to Use</h3>
1. Clone this repo in on your local machine at Desktop.<br />
2. Add your .srt file in this folder.<br />
3. Run Command Prompt(CMD) if you are on Windows.<br />
4. Run the following code in the CMD: <br />
<pre>
  cd C:\Users\%username%\Desktop
  convertSrt %fileBaseNameNoExtension%
</pre>

<h3>Example</h3>
Suppose you have a file - "titles.srt".<br />
Copy this file to your srt-convertor folder.<br />
Suppose your username is "john".<br />
So run the following code in CMD: <br />
<pre>
  cd C:\Users\john\Desktop
  convertSrt titles
</pre>

<h3>Before</h3>
<pre>
1
00:00:00,060 --> 00:00:04,850
what are you doing what are you<font color="#E5E5E5"> doing</font>

2
00:00:04,850 --> 00:00:12,330
<font color="#E5E5E5">sending</font><font color="#CCCCCC"> you a package on this</font><font color="#E5E5E5"> stream</font>

3
00:00:12,330 --> 00:00:15,389
<font color="#CCCCCC">beaver</font><font color="#E5E5E5"> you can see your ID password and</font>
</pre>

<h3>After</h3>
<pre>
what are you doing what are you doing
sending you a package on this stream
beaver you can see your ID password and
</pre>

<h3>What I Learned</h3>
<ul>
  <li>Python File Handling</li>
  <li>.BAT File Commands</li>
</ul>
