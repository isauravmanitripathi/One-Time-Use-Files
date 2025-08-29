# In-Depth Testing/ Walk-Forward Analysis

nce I have a trading system that I believe has some sort of edge to it, and it passes all the preliminary tests I throw at it, then I feel comfortable going on to more in-depth testing. As stated earlier, there are four primary ways of testing:

- Historical back testing—all in-sample
- Out-of-sample testing  $\blacksquare$
- Walk-forward testing
- Real-time testing

Over the years I have successfully and unsuccessfully used each one of these approaches. Currently, I believe that walk-forward analysis offers the best combination of amount of history that can be tested, degree of match between historical and real-time results, and sensitivity to changing market conditions. During the in-depth testing phase described in this chapter, I will use only walk-forward testing. But before we get into a discussion about walk-forward testing, what if you don't have any parameters to optimize?

# ■ **No Parameters**

 Occasionally, you may develop a system that has no parameters to optimize at all. For example, your entry may be based on a specifi c candlestick chart pattern, and your exit might be a set‐dollar‐amount stop‐loss, with a set profi t target. For whatever reason, you may decide that you never want to change these values for stop-loss and target, and you do not want to change the entry. Your philosophy may be "no optimization, ever," which is certainly one way to avoid curve fi tting or overfi tting of the system to the data.

 In situations such as this, your in‐depth analysis will simply consist of one historical test through the data. If the results meet your goals, you can simply move on to the next step. If not, you should discard the strategy and move on to the next idea.

 One important point is that if your optimizationless strategy does not work, you should not go back and tweak the strategy, followed by rerunning it. For example, if you run it the fi rst time and are displeased with the results, you should not change the entry to a diff erent candlestick pattern and try again. That is just an optimization of the entry, done a diff erent way. But it is still optimization.

 If you think this technique might apply to you, you can turn these two unique strategies into one optimizable strategy, following the pseudo code technique shown below:

#### **Strategy 1**

 Enter long with candlestick pattern A Stop‐loss \$X, profi t target \$Y

#### **Strategy 2**

 Enter long with candlestick pattern B Stop‐loss \$X, profi t target \$Y

#### **Strategy 3—strategies 1 and 2 combined**

 For i = 1 to 2 If i = 1, enter long with candlestick pattern A If i = 2, enter long with candlestick pattern B Stop‐loss \$X, profi t target \$Y

 The benefi t of such an approach is that you know up front that you are optimizing (no hidden or forgotten optimizations to taint your results), and it may very well be that a combination of strategies (e.g., strategy 1 might be better in year 1, but strategy 2 might be better in year 2) might be better than either by itself.

 If you truly decide that you have no parameters to optimize, simply substitute the walk‐forward analysis shown later for a single‐run historical analysis. If the results are favorable, you can then proceed to the next step. In most situations, though, you will have at least one parameter to optimize, and for those cases walk‐forward analysis is the best way to go.

# ■ **A Walk-Forward Primer**

 Many people are confused by walk‐forward testing and how it really is diff erent from traditional optimization. I think understanding the walk‐forward concept has been made even more diffi cult to understand by the introduction of it in most trading software packages. In the "old" days, without specialized software or a spreadsheet, walk‐forward testing had to be performed by hand or custom computer programming. In fact, when I had my successful run in the World Cup trading contest, I relied on strategies developed with walk‐forward testing conducted by hand. It was diffi cult and tedious, but it gave me a clear understanding of how the process works.

 To bring the concept down to earth, I will fi rst demonstrate the process on a simple breakout trading system. In this way, you can see step by step how the walk‐ forward analysis is done.

First, some simple defi nitions regarding the walk‐forward analysis are in order:

*In period.* This is the chunk of historical data that will be optimized.

- *Out period.* This is the chunk of historical data that will be evaluated using optimized results from the adjacent in period.
- *Fitness factor.* This is the criterion used to determine the "best" result, allowing us to select the optimized parameters.
- *Anchored/Unanchored test.* This tells us whether or not the in period start date shifts with time, or if the start date is always the same.

 Although I will discuss the details of how to select these parameters a bit later, for our test case we will use a 5‐year in period, a 1‐year out period, fi tness factor of net profi t, and an unanchored test.

Our strategy will be a very simple one: a countertrend breakout‐type system:

 Enter short if the close is an "X"‐day high close Enter long if the close is a "Y"‐day low close Stop‐loss of "Z" In TradeStation Easy Language, the system code becomes:

input: X(5), Y(5), Z(200);

if close=highest(close,X) then buy next bar at market;

if close=lowest(close,Y) then sellshort next bar at market;

 For this example, we will use the continuous contract for the mini S&P (ES), and use 10 years of data, from January 1, 2000, to January 1, 2010. We will use daily bars and include \$25 slippage and commission per round trip trade.

 For comparison purposes, fi rst we will optimize over all the data from 2000 to 2010. Using net profi t as our fi tness function criteria, we get the optimum values:

$$X = 9$$
  

$$Y = 5$$
  

$$Z = $600$$

 This complete optimization produces a net profi t of \$55,162 over the 10‐year period. Now, we will run the walk‐forward analysis. Since we are running a 5‐year optimization period, we will fi rst optimize from January 1, 2000, to January 1, 2005.

When we do this, we get the following parameters for the highest net profi t case:

 X = 7 Y = 17 Z = \$600

 That completes out fi rst in‐sample evaluation. Now we apply the preceding parameters to our fi rst out‐of‐sample period, January 1, 2005, to January 1, 2006. Note that it is considered out‐of‐sample because it was not in the fi rst optimization period. The results of this fi rst out‐of‐sample yields a loss of \$3,138.

 In a similar fashion, we then run the in‐sample optimizations, and the out‐of‐ sample performance runs for each of the rows shown in Table 13.1 .

 Once we are complete, we have our walk‐forward analysis. To create a complete performance report of the walk‐forward data, we can create a strategy where the values change every time the walk‐forward period changes. Such a strategy looks like this:

```
 var: X(5), Y(5), Z(200);
```

```
 If date>1050101 and date<1060101 then begin 
   x=7; y=17; z=600; 
 end;
```

| TABLE 13.1 | Sample Walk‐Forward Test Results |
|------------|----------------------------------|
|------------|----------------------------------|

| In‐Sample Test Period | Best Parameters X, Y, Z | Out‐of‐Sample Period | Out‐of‐Sample Result |
|-----------------------|-------------------------|----------------------|----------------------|
| 1/1/2000–1/1/2005     | 7,17,600                | 1/1/2005–1/1/2006    | −\$3,138             |
| 1/1/2001–1/1/2006     | 7,45,100                | 1/1/2006–1/1/2007    | −\$2,325             |
| 1/1/2002–1/1/2007     | 49,7,600                | 1/1/2007–1/1/2008    | +\$5,963             |
| 1/1/2003–1/1/2008     | 21,11,1000              | 1/1/2008–1/1/2009    | −\$19,113            |
| 1/1/2004–1/1/2009     | 9,5,600                 | 1/1/2009–1/1/2010    | +\$8,675             |

```
 If date>1060101 and date<1070101 then begin 
   x=7; y=45; z=100; 
 end; 
 If date>1070101 and date<1080101 then begin 
   x=49; y=7; z=600; 
 end; 
 If date>1080101 and date<1090101 then begin 
   x=21; y=11; z=1000; 
 end; 
 If date>1090101 and date<1100101 then begin 
   x=9; y=5; z=600; 
 end; 
 If date>1100101 and date<1110101 then begin 
   x=9; y=5; z=600; 
 end; 
 If date>1110101 and date<1120101 then begin 
   x=9; y=5; z=700; 
 end; 
 If date>1120101 and date<1130101 then begin 
   x=9; y=5; z=700; 
 end; 
 If date>1130101 and date<1140101 then begin 
   x=9; y=5; z=700; 
 end; 
 if close=highest(close,X) then sellshort next bar at market; 
if close=lowest(close,Y) then buy next bar at market;
 SetStopLoss(Z);
```

 This will allow us to compare the walk‐forward results to the optimized results. This is shown in Figure 13.1 . The interesting points of this comparison are:

- The optimized equity curve is much, much better than the walk‐forward curve. This is to be expected, since the optimized curve is a result of optimization. This should tell you that practically any strategy can be made to look good, if you optimize the parameters over the time period you are interested in.
- The walk‐forward results are not very good. Walk‐forward analysis is a tough test for a strategy to "pass." Most strategies fail at this analysis. But since this simulates real life more than fully optimized results do, it is a more accurate method of analysis.

![](_page_5_Figure_0.jpeg)

 **FIGURE 13.1** Walk‐Forward Results vs. Optimized Results, as Developed

 I have mentioned it a few times, but you still might be wondering, "How do you know walk‐forward analysis is more representative of future performance that the fully optimized test?" I claim this based on my experience. The current system is a good example of this performance diff erence. For the analysis just completed, here is how the optimized and walk‐forward analysis performed from January 1, 2010, to November 14, 2013. As you can see in Figure 13.2 , for the optimized case, the performance during the out‐of‐sample period 2010–2013 was fl at. It looks nothing at all like the optimized portion of the curve from 2005 to 2009, where the average annual gain was approximately \$10,000. It is a diff erent story for the walk‐forward analysis, as depicted in Figure 13.2 . The years 2010–2013 were fl at for the walk‐forward equity curve also, but it mimics the 2005–2009 walk‐forward results. In other words, the performance of the walk‐forward system did not change through the years—it was consistently fl at to down most of the years.

 While one example does not make it a rule, in general this is the kind of performance you can expect from optimized back tests and walk‐forward back tests. Optimized results, when applied to out of sample data, generally degrade. This is why so many people get frustrated with systems sold by unscrupulous vendors. These vendors show optimized results, and the performance in the future is almost never as good as the back test. Walk‐forward results, however, should perform about the same throughout the whole test period. This is why many traders prefer

![](_page_6_Figure_0.jpeg)

 **FIGURE 13.2** Walk-Forward Results vs. Optimized Results, Before and After Development

walk‐forward results. Walk‐forward analysis tends to produce equity curves that are more stable going forward. Again, that is not a rule, but it is my experience that this is generally true.

# ■ **Walk-Forward Inputs**

 If we are performing the analysis by hand, as described above, we must know the following parameters *before* we start the analysis:

 In period Out period Fitness function Method: anchored or unanchored

 In you are using software to perform the analysis (as I currently do), you do not necessarily have to know these values in advance. That is both a blessing and a curse. It is good because you only have to run the optimization once and not keep repeating the walk‐forward analysis over and over. It is bad because these parameters can be optimized, just like any traditional input parameter in your strategy. It may not seem like an optimization, at least in the traditional sense, but if you, for example, look at two values of in period, and choose the one with better results, that is still optimizing. You want to make the decision before you do the analysis.

 Assuming you will be choosing the walk‐forward inputs beforehand (we will examine an alternative method to this later), how do we choose values for each of them? A method for determining each value is described below.

## **In Period**

 For the in period, the goal is to get enough trades to make a meaningful conclusion as to the best parameters to use for each period. It makes sense, then, to get a certain amount of trades per input variable in your in period. For example, if you have four inputs to optimize, then you might want 100 to 200 trades in your in period, which would be equivalent to 25 to 50 trades per input. Unfortunately, there is no set number of trades per input that is "best," although many people say that 30 is a good number for statistical signifi cance.

## **Out Period**

 As crazy as it sounds, I know people who do walk‐forward analysis every day, which means their out period is one day. Personally, I think this is extreme, but who am I to argue if they are having success? There are a couple of factors at play in the selection of an out period. First, if you set the out period too big, you might only have one or two out periods for your walk‐forward analysis, which means the test becomes similar to a single‐period out‐of‐sample test. Second, if you set the out period too small, you will be conducting reoptimizations on a daily or weekly basis. This might not be sustainable given the limited time you likely have to develop and trade, if you have many systems to reoptimize. Knowing that there are boundaries to the out period, I generally set my out period to between 10 to 50 percent of the in period. So, if my in period is 1,000 days, my out period might be in the range of 100 to 500 days. This is a very wide range, but with robust systems you will generally see that the fi nal results are not extremely sensitive to out period. A 100‐day out period may very well perform about the same as a 500‐day out period.

# ■ **Fitness Function**

 Of all the parameters in walk‐forward analysis, the fi tness function is the most contentious. I'm sure that raucous debate by two developers over the fi tness function has at some time resulted in physical violence (such dedication to the cause!). I don't want to stir the pot by going into the pros and cons of various fi tness functions, but I will tell you the ones I have had the most success with.

## **Net Profi t**

 For many people, this is the default choice, and it is a pretty good one. After all, without profi t at the end of the test, all other parameters are meaningless. I personally use this fi tness factor the most, since it is easy to understand and implement. But it does not take into account another important results: drawdown. My experience, however, has been that in general high net profi t runs hand in hand with low maximum drawdown. If you decide drawdown is a must have, then one of the fi tness function below should suit you.

## **Linearity of Equity Curve**

 Think for a minute of your ideal equity curve. The equity would go up every day, and it would be consistent. A real‐world example is interest on a banking or money market account. Interest earned might be very small, but with a bank account, you make money every day, and there is never a day where you lose money. If only you could design a futures system that made money every day, with never a drawdown! A linear, upward‐sloping equity curve is the ideal, and is a great parameter to optimize for. The problem is that, unless your software includes this fi tness function as a set choice, it may be diffi cult in actual practice to actually optimize for it. Also, it may be diffi cult to implement in a nonanchored walk‐forward test. Finally, this method of optimization may select very low net profi t iterations as the optimum, since they may exhibit the most linearity. There are two potential problems with the low‐profi t cases: fi rst, since there is not much profi t, if you underestimate your slippage and commissions, you might actually be selecting a real‐time losing strategy. Second, if the end result is very small average profi t per trade, minor changes in the market may render your eff ective ineff ective.

 One big plus to using a linear equity curve as your optimization criteria is that it is very good for position sizing. Think about a strategy where your drawdowns are minimal and your profi ts are slow and steady. Such an approach would be ideal for aggressive position sizing.

## **Return on Account**

 If you explicitly use maximum drawdown in your fi tness function, then return on account is a good option. Although some software packages vary in their defi nition, return on account is generally defi ned as:

```
 Return on Account = Net Profi t/(Maximum Drawdown + Required Margin)
```

 Since required margin varies over time, many people just eliminate this from the calculation by assuming it is equal to zero or some other arbitrary value. As a fi tness function, return on account is nice to use, since it takes into account both the profi t, and the risk it took to get that profi t. The biggest drawback to using it is that it can give wildly diff erent results from period to period using unanchored walk‐forward analysis.

# ■ **Anchored/Unanchored**

 One subtle aspect of walk‐forward analysis is the optimization window. You can go one of two ways with this window: you can move it with time, or you can keep the start point anchored. Figure 13.3 shows the diff erence between these two approaches.

 In general, the two methods will give similar results, especially at the beginning of the analysis. But as time goes on, the results will tend to diverge. This is because the anchored walk‐forward is always taking into account results over the whole data set, while the unanchored results include results for only the most recent window. There may be times where one is more appropriate than the other, but I tend to use the unanchored method much more. I like that approach, since it ensures that only the most recent data is included in the optimization. I don't necessarily want results from 10 years ago still impacting my optimization results today.

 One point of caution with using unanchored data, with certain fi tness functions, is that the results you get might be faulty, depending on your walk‐forward analysis software. If you are using a manual method, this should not be a problem, but if you use software, make sure that the calculations are based on the start and end dates in question, not on diff erence in fi tness functions during the period.

|                      | 2007 | 2008 | 2009 | 2010 | 2011 | 2012 | 2013 |
|----------------------|------|------|------|------|------|------|------|
| Anchored Test        |      |      |      |      |      |      |      |
| Anchored in sample 1 |      |      |      |      |      |      |      |
| Walk-forward 1       |      |      |      |      |      |      |      |
| Anchored in sample 2 |      |      |      |      |      |      |      |
| Walk-forward 2       |      |      |      |      |      |      |      |
| Anchored in sample 3 |      |      |      |      |      |      |      |
| Walk-forward 3       |      |      |      |      |      |      |      |
|                      |      |      |      |      |      |      |      |
| Unanchored Test      |      |      |      |      |      |      |      |
| In sample 1          |      |      |      |      |      |      |      |
| Walk-forward 1       |      |      |      |      |      |      |      |
| In sample 2          |      |      |      |      |      |      |      |
| Walk-forward 2       |      |      |      |      |      |      |      |
| In sample 3          |      |      |      |      |      |      |      |
| Walk-forward 3       |      |      |      |      |      |      |      |

 **FIGURE 13.3** Anchored vs. Unanchored Walk‐Forward Analysis

|                     |            |              | Return on Account = Net Profit/ |
|---------------------|------------|--------------|---------------------------------|
| Optimization Period | Net Profit | Max Drawdown | Max Drawdown                    |
| Year 1              | \$12,000   | \$6,000      | 2.0                             |
| Year 2              | \$6,000    | \$4,000      | 1.5                             |
| Year 1– Year 2      | \$18,000   | \$6,000      | 3.0                             |

 **TABLE 13.2 Many Performance Metrics Are Not Additive**

 A simple example explains it well. Suppose you have the optimized results shown in Table 13.2.

 Note in this example that while net profit is additive (the net profit in year 1 plus the net profit in year 2 equals the combined net profit for year 1 + year 2), the maximum drawdown and return on account are not. Some walk‐forward software packages may assume your fitness function is additive (like net profit), so make sure you understand how the software works when using unanchored results. Your analysis could be completely flawed depending on the fitness function you choose.

# ■ **Running the Analysis**

 Once you have all your walk‐forward inputs defi ned, you simply run the analysis manually as I have shown in the earlier example, or automatically with the software. Either way, in the end, you will have the completed walk‐forward analysis and equity curve for your strategy. At this point, you have to compare the results to your goals and objectives. If the system passes, you of course go on to the next step. If it fails, theoretically you should discard the strategy and start with something diff erent. In reality, of course, that is extremely diffi cult to do. You have already invested a great deal of time in preliminary testing and in‐depth testing, and it seems a shame that you should just discard your work. This is especially true if the results are close to your goal. Maybe lowering the goal or making a small change to the strategy and rerunning walk‐forward might be the path to success. Or does that just lead to more bad habits and decisions?

 In general, I normally would discard a strategy at this point, rather than compromise my goals or change my strategy. But sometimes I do one or both of these things. Occasionally, that turned out to be a good decision, but likely more often than not it did not work out well. Remember, the more you touch (test) historical data, the more likely you are to fi t your system to the data. Plus, when you relax your standards, you end up with something you really did not want. When real money is on the line, this may become a major point of contention for your psyche—why continue to trade a currently losing system that you had doubts about in the fi rst place?

 One common mistake during walk‐forward analysis is to surreptitiously optimize the *in* and *out* periods. Say, for example, that you run the walk‐forward analysis with four‐year in period, and one‐year out period. Walk‐forward results for that case are good, but not great, so you think "maybe I should use four years in, with two years out." That case is 200 percent better and meets all your goals, so you decide "that's the combination to use. Let's go!"

Stop.

 Do you realize what just happened? As soon as you selected a second set of in/out parameters, reran the results, and selected the best case, you just optimized. Sure, it is not a full optimization, since you only compared two cases, but it was optimization nevertheless. Remembering the rule that optimized results can't be trusted, you have a dilemma here: accept the fi rst run (4 year/1 year), and then discard the strategy because it did not meet your goals, or accept the second run, and pretend you never optimized.

 Once again, I'll admit to doing the above on occasion, although I can't recall it ever ending well. The big question in all this is "is there a way to test multiple in/out periods, and select the best one, while still maintaining walk‐forward integrity?" The answer, thankfully, is yes. The way to do it is to create, in essence, a second walk‐ forward analysis inside of the fi rst. The way to do this is to run the walk‐forward analysis, as usual, but leave the last few years of data untouched. I typically will leave three years untouched. Then, with the walk‐forward data I have, I select the best in/ out pair I have, and then run it on the last three years of data. If it passes, then I go on to the next step. If it doesn't, I discard the strategy. But, in either case, at least I have made some eff ort to select the best in/out combination. The downside to this approach is that you have optimized, and the more optimization you do, the worse off you generally are.

This process would look like this:

- 1. Years 2000–2008 >> run walk‐foward analysis for diff erent combinations of in/out periods, select the best in/out.
- 2. Years 2009–present >> run walk‐forward analysis, using best in/out determined from Step 1.
- 3a. If walk‐forward results from 2009–present look good, continue with development.
- 3b. If results do not look good, it is probably best to abandon strategy, rather than try again with another in/out pair.

 Figure 13.4 depicts the approach of optimizing in/out periods, compared to a traditional walk‐forward analysis.

![](_page_12_Figure_0.jpeg)

FIGURE 13.4 Walk-Forward Test, Inside Another Walk-Forward Test

## Put the Walk-Forward Strategy Together

Once you have completed the walk-forward analysis, analyzed the results, and found that your results compare favorably to your objectives, you are almost ready for the next step. There is just one more check to run, and that is with the completed walkforward history strategy. The difference between the walk-forward history strategy and the optimizable strategy is shown next:

#### Optimizable Strategy

input: avg(10); // strategy code

#### Walk-Foward History Strategy

```
var: avg(10);
If date is between Jan 1, 2010 and Jan 1, 2011 then
avg=8If date is between Jan 1, 2011 and Jan 1, 2012 then
avg=12If date is between Jan 1, 2012 and Jan 1, 2013 then
avg=6<pre>// strategy code</pre>
```

The strategy with the walk-forward history changes the variables based on the date. In this way, you will have a seamless history for your strategy to run; you will not have to cut and paste results together to create the walk-forward history.

 Note that the results you get from this strategy might be diff erent from the results of a piece‐by‐piece analysis method. This is especially true for swing strategies that last for days or weeks. The reason this is so is that, based on the walk‐forward parameters, variables might change in the middle of a trade, causing trades to be exited or reversed. To see if this is important for your strategy, then, it becomes critical to create a stand‐alone walk‐forward history strategy.