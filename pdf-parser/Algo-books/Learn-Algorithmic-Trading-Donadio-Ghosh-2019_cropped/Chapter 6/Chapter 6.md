# <span id="page-0-0"></span>**Section 4: Building a Trading System**

In this section, you will learn how the trading algorithm we are building interacts with the different actors in the trading arena. You will learn how to build a trading bot from scratch. Using the algorithm constructed in the previous sections, you will learn how to implement it, where to connect it, and how to handle it.

This section comprises the following chapters:

- [Chapter 7](#page-0-0), *Building a Trading System in Python*
- Chapter 8, *Connecting to Trading Exchanges*
- Chapter 9, *Creating a Backtester in Python*

# **Building a Trading System in Python**

In the initial chapters of this book, we learned how to create a trading strategy by analyzing historical data. In this chapter, we are going to study how to convert data analysis into real-time software that will connect to a real exchange to actually apply the theory that you've previously learned.

We will describe the functional components supporting the trading strategy based on the algorithm created in the previous chapters. We will be using Python to build a small trading system. We will use the algorithms to build a trading system capable of trading.

This chapter will cover the following topics:

- Understanding the trading system
- Building a trading system in Python
- Designing a limit order book

## **Understanding the trading system**

A trading system will help you to automate your trading strategy. When you choose to build this kind of software, you need to take the following into consideration:

- **Asset class**: When you code, knowing which asset class will be used in your trading system will modify the data structure of this software. Each asset class is idiosyncratic and has its own set of features. US stocks are mainly traded on two exchanges (NY Stock Exchange and NASDAQ). There are about 6,000 companies (symbols) listed on these two exchanges. Unlike equities, **Foreign Exchange** (**FX**) has six major currency pairs, six minor currency pairs, and six more exotic currency pairs. We can add more currency pairs, but there will not be more than 100 currency pairs. However, there will be hundreds of market players (banks, brokers).
- **Trading strategy type (high frequency, long-term position)**: Depending upon the type of strategies, the design of the software architecture will be impacted. High-frequency trading strategies require sending orders very rapidly. A regular trading system for US equities will decide to send an order within microseconds. A system trading on the Chicago Mercantile Exchange (CME) could work within nanoseconds. Based on this observation, the technology will be critical in the choice of designing the software. If we just refer to the programming language, Python is not adapted to speed and we will preferably choose C++ or Java. If we want to take a long-term position such as many days, the speed allowing a trader to get a liquidity faster than others will not be important. A programming language such as Python will be fast enough to reach this goal.
- **The number of users (the number of trading strategies)**: When the number of traders increases, the number of trading strategies increases. This means that the number of orders is higher. Before sending an order to an exchange, we need to check the validity of the orders we are about to send: checking whether the overall position for a given instrument has not been reached. In trading world, we have more and

more regulations moderating trading strategies. To follow that our trading strategy respect the regulation, we will test the compliance of the orders that we want to send. All these checks will add some calculation time. If we have too many orders, we will need to have all these verification done sequentially for one given instrument. If the software is not fast enough, it will slow down the orders to go out. So having more users will require a faster trading system.

These parameters modify the conception of the trading system you are going to build. It is essential to have a clear description of the requirements when you build a trading system.

Because the goal of a trading system is to support your trading ideas. The trading system will collect the information that your trading strategy needs and be in charge of sending orders and receiving responses from the market regarding this order. The main functionalities will be to collect the data (most of the time this will be price updates). If the trading strategy needs to get some quantitative data involving earnings, fed announcements (more generally news), these news will also trigger orders. When the trading strategy decide the direction of the position. the trading system will send orders accordingly . The trading system will also decide which specific exchange will be the best to get the order filled for the requested price and for the requested volume.

## **Gateways**

A trading system collects price updates and sends orders on your behalf. In order to get to that, you need to code all the steps that you would do if you were trading without any trading system. If you would like to make money by buying low and selling high, you will need to choose the product you will use to trade. Once you select this product, you want to receive the order from the other traders. The other traders will provide you their intention (their orders) to trade a financial asset by indicating the side, the price and the quantity. As soon as you receive enough orders for the product that you want to trade, you can choose the trader you are going to make a deal with. You will make your decision based on the price of this asset. If you want to resell this asset later one, it will be important to buy it for a low price. When you agree with a price, you will indicate the other trader that you will want to buy for the advertised price. When the deal is done, you now own this product. You will proceed the same way when you want to sell it at a higher price. We formalize this way of trading using functional units:

**Data handling**: Collecting price updates coming from the venues you will choose to trade with (exchanges, ECNs, dark pools). This component (called a **gateway** in the following diagram) is one of the most critical of the trading system. The task of this component is to get the book for a given instrument from an exchange to the trading system. This component will be linked to the network and it will get connected to exchanges receiving and sending streams to communicate with it.

The following diagram represents the location of the gateways in the trading system. They are the input and the output of the trading system:

![](_page_5_Figure_0.jpeg)

The diagram shows the following:

- The venues represent traders, exchanges, ecns, and dark pools.
- The getaways and venues can be linked by different ways (they are represented using arrows).
- We can use a wire, wireless network, internet, microwave, or fibers. All these different network media have different characteristics in terms of speed, data loss, and bandwidth.
- We can observe the arrows are bidirectional for the price updates and the orders. There is a protocol to ask for price updates.
- The gateway will initiate a network connection with the venue, authenticate itself, and subscribe to a given instrument to start receiving

price updates (we will explain this part in more detail later).

- The gateway taking care of orders also receives and send messages. When an order is created, it is sent through the network to the venue.
- If the venue receives this order, an acknowledgment of this order will be sent. When this order has met a matching order, a trade will be sent to the trading system.

## **Order book management**

The main task of data handling is to replicate the limit order book from the venues into your trading system. To combine all the different books you receive, the **book builder** will be in charge of gathering the prices and sorting them for your strategies.

In the following diagram, the price updates are converted by the gateway then transferred to the book builder. The book builder will use the books received by the gateways from the venues and it will gather and sort all the price updates:

![](_page_8_Figure_0.jpeg)

In the following diagram, we use an example of an **order book** for a given financial product. Since we have three venues, we observe three different books:

![](_page_9_Figure_0.jpeg)

The diagram shows the following:

- In these books, you can see for each row there is an order.
- For instance, in the bid list of Venue 1, there is a trader willing to buy 1,000 shares for \$1.21. On the other side is the list of people willing to sell.
- You can expect the offer (or ask) price to always be higher than the bid price.
- Indeed, if you could buy for a smaller amount than you could sell, it would be too easy to make money.
- The task of the book builder is to get the three books from the three venues collected by the gateways. The book builder regroups the three books and sort the orders.

# **Strategy**

The trading strategy is the brain of the system. This is where your algorithm representing your trading idea will be implemented. Let's have a look at the diagram:

![](_page_10_Figure_2.jpeg)

The diagram shows the following:

- The trading strategy is divided into two main components: **signal** and **execution**. In this book, the numerous strategies we saw in the first part can be called signal.
- The signals represent the indication of getting a long or a short position. For instance, in the dual moving average crossover momentum strategy, when the two average lines were crossing, a signal to go long or go short was generated.

- The signal component of this strategy only focuses on generating signals. However, having the intention (a signal) does not guarantee you to get the liquidity you are interested in. For instance, in highfrequency trading, it is highly likely your orders will be rejected because of the speed of your trading system.
- The execution part of the strategy will take care of handling response from the market. This part decides what to do for any responses from the market. For instance, what should happen when the order is rejected? You should continue trying to get an equivalent liquidity, another price. That's an important part you will need to focus how to implement.

### **Order management system**

The **order management system** (**OMS)** is the component that collects the orders sent from the strategies. The OMS keeps track of the order life cycle (creation, execution, amendment, cancelation, and rejection). Trading strategy orders are gathered in the OMS. The OMS may reject orders if an order is malformed or not valid (too large a quantity, wrong direction, erroneous prices, excessive outstanding position, or order type not handled by the exchange). When an error is detected in the OMS, the order does not go out from the trading system. The rejection happens earlier. Consequently, the trading strategy can respond faster than if the order was rejected by the exchange. Let's have a look at the following diagram, which illustrates these features of the OMS:

![](_page_12_Figure_2.jpeg)

# **Critical components**

Gateways, a book builder, strategies, and an OMS are the critical components of any trading system. They gather the essential functions you need to start trading. We measure the performance of a trading system in terms of speed by adding the processing time of all the critical components. We start a timer when a price update gets into the entrance of the trading system and we stop the timer when the order triggered by this price update goes out from the system. This time is called the **tick-to-trade** or **tick-toorder**.

In the most recent systems, this time is in the order of microseconds (around 10 microseconds). When optimized with special hardware and software programming, this time can even be reduced to nanoseconds (around 300 nanoseconds). Because we choose to use Python to implement our trading system, the tick-to-trade of this Python system will be in the order of milliseconds.

## **Non-critical components**

The non-critical components are the components not directly linked with the decision to send an order. They modify parameters, report data, and gather data. For instance, when you design a strategy, you will have a set of parameters that you need to adjust in real time. You need a component capable of conveying the information to the trading strategy component. For that, we will have a component called **command and control**.

## **Command and control**

Command and control is an interface between traders and the trading system. It can be a command-line system or a user interface receiving the commands from the traders and sending the messages to the appropriate components. Let's have a look at the following diagram:

![](_page_15_Figure_2.jpeg)

As shown in the diagram, if we need to update the trading strategy parameters, the trader can use a text field on a web-based application to specify the risk tolerance the trading strategy can take. The number (corresponding to the tolerance limit) will be sent to the appropriate trading strategy.

## **Services**

Additional components may be added to the trading system. We will talk about the following components (it is not an exhaustive list):

- **Position server**: This keeps track of all the trades. It updates the positions for all the traded financial assets. For instance, if a trade is made for 100,000 EUR/USD at a price of \$1.2, the notional position will be \$120,000. If a trading system component needs the position amount for EUR/USD, it will subscribe the position server for getting position updates. The order manager or the trading strategy may want to know this information before allowing an order to go out. If we want to limit the position to \$200,000 for a given asset, another order to get 100,000 EUR/USD will be rejected.
- **Logging system**: This gathers all the logs from the components and will write a file or modify a database. A logging system helps with debugging, figuring out causes of issues, and also just reports.
- **Viewers** (read-only user interface view): These display the views for trading (positions, orders, trades, task monitoring, and so on).
- **Control viewers** (interactive user interface): These provide a way to modify parameters and start/stop components of the trading system.
- **News server**: This gathers news from many news companies (such as Bloomberg, Reuters, and Ravenpack) and provides this news in real time or on demand to the trading system.

# **Building a trading system in Python**

In this section, we will describe how to create a trading system from scratch. We will use Python to code this trading system but the approach is general enough to be transferred to other languages. We will talk about the design and the best software engineering practice. The system we will create will have the bare minimum components to trade and you may want to extend it after this first initial implementation.

Python is an object-oriented language. We will encapsulate the main functionalities of the trading system into Python objects. We will have these components communicate through channels. We will simplify the functional components by limiting this first implementation to five main components. We will code these five components into five different files. We will associate unit tests to all these components:

- 1-py: We will reproduce the behavior of liquidity providers. In this example, it sends price updates (orders).
- 2-py: To simplify the design, we are removing the gateway and we will plug the liquidity provider directly to the order book manager. This component will be in charge of building a book.
- 3-py: This file contains the trading strategy code.
- 4-py: This contains the code for the order manager.
- 5-py: This replicates the behavior of a market:

![](_page_18_Figure_0.jpeg)

We observe from the preceding diagram that there are links between all the components. Every link is a unidirectional communication channel. In Python, the data structure we choose is a deque from the collections package.

We use two methods of the deque data structure:

- push: This inserts an element into the channel.
- popleft: This removes an element from the channel.

We will first describe the implementation of all these components one by one. We will describe the public methods that will be used to use them. When you start designing a class, you first need to know what this class is supposed to do. You will design the testing environment that will be able verify the component behavior.

The orders and the order updates will be represented by a simple Python dictionary. Let's have a look at the code:

```
ord = {
 'id': self.order_id,
 'price': price,
```

```
 'quantity': quantity,
 'side': side,
 'action': action
 }
```

#### **LiquidityProvider class**

The LiquidityProvider class is the simplest of all the others. The goal of this component is to generate liquidities. Since we randomly generate liquidities, we just need to test whether the first liquidity that is sent by the LiquidityProvider class is well formed. We will create the generate\_random\_order function, which will randomly pick a side, a price, a quantity, and an action associated to this order. We will have three kinds of actions: create a new order, amend an order, and cancel an order. Since we are going to create a full trading system, we will also want to test the full system by inserting the order manually. Hence, this LiquidityProvider component will have a way to insert manual orders into the system.

The following code describes the LiquidityProvider class. We will use a pseudo random generator initialized by a seed. When you run your code several times, a seed will allow you to make the random number deterministic.

The generate\_random\_order function uses the lookup\_orders function to determine whether the next order that will be generated already exists:

1. In the code, we will create the LiquidityProvider class. The goal of this class is to act as a liquidity provider or an exchange. It will send price updates to the trading system. It will use the lp\_2\_gateway channel to send the price updates:

```
from random import randrange
from random import sample, seed
class LiquidityProvider:
 def __init__(self, lp_2_gateway=None):
 self.orders = []
 self.order_id = 0
 seed(0)
 self.lp_2_gateway = lp_2_gateway
```

2. Here, we create a utility function to look up orders in the list of orders:

```
 def lookup_orders(self,id):
 count=0
 for o in self.orders:
 if o['id'] == id:
 return o, count
 count+=1
 return None, None
```

3. The insert\_manual\_order function will insert orders manually into the trading system. As shown, this function will be used for unit testing some components:

```
 def insert_manual_order(self,order):
 if self.lp_2_gateway is None:
 print('simulation mode')
```

```
 return order
 self.lp_2_gateway.append(order.copy())
```

The generate\_random\_order function will generate orders randomly. There will be three types of orders:

- New (we will create a new order ID)
- Modify (we will use the order ID of an order that was created and we will change the quantity)
- Delete (we will use the order ID and we will delete the order)
- 4. Each time we create a new order, we will need to increment the order ID. We will use thelookup\_orders function as shown in the following code to check whether the order has already been created:

```
 def generate_random_order(self):
 price=randrange(8,12)
 quantity=randrange(1,10)*100
 side=sample(['buy','sell'],1)[0]
 order_id=randrange(0,self.order_id+1)
 o=self.lookup_orders(order_id)
 new_order=False
 if o is None:
 action='new'
 new_order=True
 else:
 action=sample(['modify','delete'],1)[0]
 ord = {
 'id': self.order_id,
 'price': price,
 'quantity': quantity,
 'side': side,
 'action': action
 }
 if not new_order:
 self.order_id+=1
 self.orders.append(ord)
 if not self.lp_2_gateway:
 print('simulation mode')
 return ord
 self.lp_2_gateway.append(ord.copy())
```

5. We test whether the LiquidityProvider class works correctly by using unit testing. Python has the unittest module . As shown, we will create the TestMarketSimulator class, inheriting from TestCase:

```
import unittest
from chapter7.LiquidityProvider import LiquidityProvider
class TestMarketSimulator(unittest.TestCase):
 def setUp(self):
 self.liquidity_provider = LiquidityProvider()
 def test_add_liquidity(self):
 self.liquidity_provider.generate_random_order()
 self.assertEqual(self.liquidity_provider.orders[0]['id'],0)
```

```
 self.assertEqual(self.liquidity_provider.orders[0]['side'], 'buy')
 self.assertEqual(self.liquidity_provider.orders[0]['quantity'], 700)
 self.assertEqual(self.liquidity_provider.orders[0]['price'], 11) OrderBook class
```

As shown, we have coded the test\_add\_liquidity function:

- This function tests whether the random generation of a liquidity functions by comparing values generated by this function to expected values.
- We used the functions belonging to this TestCase class to make a test fail if the returned values are not the expected ones.
- This code will generate an order and test the order characteristics. If one field value is not the expected one, the unit test will fail.

#### **Strategy class**

This class represents the trading strategy based on top of the book changes. This trading strategy will create an order when the top of the book is crossed. This means when there is a potential arbitrage situation. When the bid value is higher than the ask value, we can send an order to buy and sell at the same time and make money out of these two transactions.

This class is divided into two parts:

- **Signal part**: This part handles the trading signal. In this example, a signal will be triggered when the top of the book is crossed.
- **Execution part**: This part handles the execution of the orders. It will be responsible of managing the order life cycle.

The following are the steps for the strategy class:

1. As shown in the following code, we will create the TradingStrategy class. This class will have three parameters. They are references to the three communication channels. One is taking the book events form the order book, the two others are made to send orders and receive order updates from the market:

```
class TradingStrategy:
 def __init__(self, ob_2_ts, ts_2_om, om_2_ts):
 self.orders = []
 self.order_id = 0
 self.position = 0
 self.pnl = 0
 self.cash = 10000
 self.current_bid = 0
 self.current_offer = 0
 self.ob_2_ts = ob_2_ts
 self.ts_2_om = ts_2_om
 self.om_2_ts = om_2_ts
```

2. We will code two functions to handle the book events from the order book as shown in the code; handle\_input\_from\_bb checks whether there are book events in deque ob\_2\_ts and will call the handle\_book\_event function:

```
def handle_input_from_bb(self,book_event=None):
 if self.ob_2_ts is None:
 print('simulation mode')
 self.handle_book_event(book_event)
 else:
 if len(self.ob_2_ts)>0:
 be=self.handle_book_event(self.ob_2_ts.popleft())
 self.handle_book_event(be)
```

**def** handle\_book\_event(self,book\_event):

```
 if book_event is not None:
 self.current_bid = book_event['bid_price']
 self.current_offer = book_event['offer_price']
 if self.signal(book_event):
 self.create_orders(book_event
 ,min(book_event['bid_quantity'],
 book_event['offer_quantity']))
 self.execution()
```

The handle\_book\_event function calls the function signal to check whether there is a signal to send an order.

3. In this case, the signal verifies whether the bid price is higher than the ask price. If this condition is verified, this function returns True. The

handle\_book\_event function in the code will create an order by calling the create\_orders function:

```
def signal(self, book_event):
 if book_event is not None:
 if book_event["bid_price"]>\
 book_event["offer_price"]:
 if book_event["bid_price"]>0 and\
 book_event["offer_price"]>0:
 return True
 else:
 return False
 else:
 return False
```

4. The create\_orders function from the code creates two orders. When we have an arbitrage situation, we must trade fast. Therefore, the two orders must be created simultaneously. This function increments the order ID for any created orders. This order ID will be local to the trading strategy:

```
def create_orders(self,book_event,quantity):
 self.order_id+=1
 ord = {
 'id': self.order_id,
 'price': book_event['bid_price'],
 'quantity': quantity,
 'side': 'sell',
 'action': 'to_be_sent'
 }
 self.orders.append(ord.copy())
 price=book_event['offer_price']
 side='buy'
 self.order_id+=1
 ord = {
 'id': self.order_id,
 'price': book_event['offer_price'],
 'quantity': quantity,
 'side': 'buy',
 'action': 'to_be_sent'
 }
 self.orders.append(ord.copy())
```

The function execution will take care of processing orders in their whole order life cycle. For instance, when an order is created, its status is *new*. Once the order has been sent to the market, the market will respond by acknowledging the order or reject the order. If the other is rejected, this function will remove the order from the list of outstanding orders.

5. When an order is filled, it means this order has been executed. Once an order is filled, the strategy must update the position and the PnL with the help of the code:

```
def execution(self):
 orders_to_be_removed=[]
 for index, order in enumerate(self.orders):
 if order['action'] == 'to_be_sent':
 # Send order
 order['status'] = 'new'
 order['action'] = 'no_action'
 if self.ts_2_om is None:
 print('Simulation mode')
 else:
 self.ts_2_om.append(order.copy())
 if order['status'] == 'rejected':
 orders_to_be_removed.append(index)
 if order['status'] == 'filled':
 orders_to_be_removed.append(index)
 pos = order['quantity'] if order['side'] == 'buy' else -order['quantity']
 self.position+=pos
 self.pnl-=pos * order['price']
 self.cash -= pos * order['price']
 for order_index in sorted(orders_to_be_removed,reverse=True):
 del (self.orders[order_index])
```

6. The handle\_response\_from\_om and handle\_market\_response functions will collect the information from the order manager (collecting information from the market) as shown in the following code:

```
 def handle_response_from_om(self):
 if self.om_2_ts is not None:
 self.handle_market_response(self.om_2_ts.popleft())
 else:
 print('simulation mode')
def handle_market_response(self, order_execution):
 order,_=self.lookup_orders(order_execution['id'])
 if order is None:
 print('error not found')
 return
 order['status']=order_execution['status']
 self.execution()
```

7. The lookup\_orders function in the following code checks whether an order exists in the data structure gathering all the orders and return this order:

```
def lookup_orders(self,id):
 count=0
 for o in self.orders:
 if o['id'] == id:
 return o, count
```

```
 count+=1
 return None, None
```

Testing the trading strategy is critical. You need to check whether the trading strategy will place the correct orders. The test\_receive\_top\_of\_book test case verifies whether the book event is correctly handled by the trading strategy. The test\_rejected\_order and test\_filled\_order test cases verify whether a response from the market is correctly handled.

8. The code will create a setUp function, being called each time we run a test. We will create TradingStrategy each time we invoke a test. This way of doing it increases the reuse of the same code:

```
import unittest
from chapter7.TradingStrategy import TradingStrategy
class TestMarketSimulator(unittest.TestCase):
 def setUp(self):
 self.trading_strategy= TradingStrategy()
```

The first unit test that we perform for a trading strategy is to validate that the book event sent by the book is received correctly.

9. We will create a book event manually and we will use the handle\_book\_event function. We are going to validate the fact that the trading strategy behaves the way it is supposed to by checking whether the orders produced were expected. Let's have a look at the code:

```
 def test_receive_top_of_book(self):
 book_event = {
 "bid_price" : 12,
 "bid_quantity" : 100,
 "offer_price" : 11,
 "offer_quantity" : 150
 }
 self.trading_strategy.handle_book_event(book_event)
 self.assertEqual(len(self.trading_strategy.orders), 2)
 self.assertEqual(self.trading_strategy.orders[0]['side'], 'sell')
 self.assertEqual(self.trading_strategy.orders[1]['side'], 'buy')
 self.assertEqual(self.trading_strategy.orders[0]['price'], 12)
 self.assertEqual(self.trading_strategy.orders[1]['price'], 11)
 self.assertEqual(self.trading_strategy.orders[0]['quantity'], 100)
 self.assertEqual(self.trading_strategy.orders[1]['quantity'], 100)
 self.assertEqual(self.trading_strategy.orders[0]['action'], 'no_action')
 self.assertEqual(self.trading_strategy.orders[1]['action'], 'no_action')
```

The second test performed is to verify whether the trading strategy receives the market response coming from the order manager.

10. We will create a market response indicating a rejection of a given order. We will also check whether the trading strategy removes this order from the list of orders belonging to the trading strategy:

```
 def test_rejected_order(self):
 self.test_receive_top_of_book()
 order_execution = {
 'id': 1,
 'price': 12,
 'quantity': 100,
 'side': 'sell',
 'status' : 'rejected'
 }
 self.trading_strategy.handle_market_response(order_execution)
 self.assertEqual(self.trading_strategy.orders[0]['side'], 'buy')
 self.assertEqual(self.trading_strategy.orders[0]['price'], 11)
 self.assertEqual(self.trading_strategy.orders[0]['quantity'], 100)
 self.assertEqual(self.trading_strategy.orders[0]['status'], 'new')
```

11. The last part, we need to test the behavior of the trading strategy when the order is filled. We will need to update the position, the pnl, and the cash that we have to invest as shown in the following code:

```
 def test_filled_order(self):
 self.test_receive_top_of_book()
 order_execution = {
 'id': 1,
 'price': 11,
 'quantity': 100,
 'side': 'sell',
 'status' : 'filled'
 }
 self.trading_strategy.handle_market_response(order_execution)
 self.assertEqual(len(self.trading_strategy.orders),1)
 order_execution = {
 'id': 2,
 'price': 12,
 'quantity': 100,
 'side': 'buy',
 'status' : 'filled'
 }
 self.trading_strategy.handle_market_response(order_execution)
 self.assertEqual(self.trading_strategy.position, 0)
 self.assertEqual(self.trading_strategy.cash, 10100)
 self.assertEqual(self.trading_strategy.pnl, 100)
```

Next, we will look at working with the OrderManager class.

## **OrderManager class**

The purpose of the order manager is to gather the orders from all the trading strategies and to communicate this order with the market. It will check the validity of the orders and can also keep track of the overall positions and PnL. It can be a safeguard against mistakes introduced in trading strategies.

This component is the interface between the trading strategies and the market. It will be the only component using two inputs and two outputs. The constructor of this class will take four arguments representing these channels:

```
class OrderManager:
 def __init__(self,ts_2_om = None, om_2_ts = None,
 om_2_gw=None,gw_2_om=None):
 self.orders=[]
 self.order_id=0
 self.ts_2_om = ts_2_om
 self.om_2_gw = om_2_gw
 self.gw_2_om = gw_2_om
 self.om_2_ts = om_2_ts
```

The four following functions will help with reading data from the channels and it will call the proper functions.

The handle\_input\_from\_ts function checks whether the ts\_2\_om channel has been created. If the channel has not been created, it means that we will use the class for unit testing only. To get new orders into the OrderManager system, we check whether the size of the ts\_2\_om channel is higher than 0. If there is an order in the channel, we remove this order and we call the

```
handle_order_from_tradinig_strategy function:
```

```
def handle_input_from_ts(self):
 if self.ts_2_om is not None:
 if len(self.ts_2_om)>0:
 self.handle_order_from_trading_strategy(self.ts_2_om.popleft())
 else:
 print('simulation mode')
```

The handle\_order\_from\_trading\_strategy function handles the new order coming from the trading strategies. For now, the OrderManager class will just get a

copy of the order and store this order into a list of orders:

```
def handle_order_from_trading_strategy(self,order):
 if self.check_order_valid(order):
 order=self.create_new_order(order).copy()
 self.orders.append(order)
 if self.om_2_gw is None:
 print('simulation mode')
 else:
 self.om_2_gw.append(order.copy())
```

Once we take care of the order side, we are going to take care of the market response. For this, we will use the same method we used for the two prior functions. The handle\_input\_from\_market function checks whether the gw\_2\_om channel exists*.* If that's the case, the function reads the market response object coming from the market and calls the

```
handle_order_from_gateway function:
```

```
def handle_input_from_market(self):
 if self.gw_2_om is not None:
 if len(self.gw_2_om)>0:
 self.handle_order_from_gateway(self.gw_2_om.popleft())
 else:
 print('simulation mode')
```

The handle\_order\_from\_gateway function will look up in the list of orders created by the handle\_order\_from\_trading\_strategy function. If the market response corresponds to an order in the list, it means that this market response is valid. We will be able to change the state of this order. If the market response doesn't find a specific order, it means that there is a problem in the exchange between the trading system and the market. We will need to raise an error:

```
def handle_order_from_gateway(self,order_update):
 order=self.lookup_order_by_id(order_update['id'])
 if order is not None:
 order['status']=order_update['status']
 if self.om_2_ts is not None:
 self.om_2_ts.append(order.copy())
 else:
 print('simulation mode')
 self.clean_traded_orders()
 else:
 print('order not found')
```

The check\_order\_valid function will perform regular checks on an order. In this example, we will check that the quantity and price are not negative.

You may consider adding more code and to check the position, PnL, or anything you consider important for your trading strategy:

```
def check_order_valid(self,order):
 if order['quantity'] < 0:
 return False
 if order['price'] < 0:
 return False
 return True
```

The create\_new\_order, lookup\_order\_by\_id, and clean\_traded\_orders functions will create an order based on the order sent by the trading strategy, which has a unique order ID. Indeed, each trading strategy can have its own local order ID. It is important that the orders we send to the market have an unique order ID. The second function will help with looking up the order from the list of outstanding orders. The last function will clean the orders that have been rejected, filled, or canceled.

The create\_new\_order function will create a dictionary to store the order characteristics:

```
def create_new_order(self,order):
 self.order_id += 1
 neworder = {
 'id': self.order_id,
 'price': order['price'],
 'quantity': order['quantity'],
 'side': order['side'],
 'status': 'new',
 'action': 'New'
 }
 return neworder
```

The lookup\_order\_by\_id function will return a reference to the order by looking up by order ID:

```
def lookup_order_by_id(self,id):
 for i in range(len(self.orders)):
 if self.orders[i]['id']==id:
 return self.orders[i]
 return None
```

The clean\_traded\_orders function will remove from the list of orders all the orders that have been filled:

```
def clean_traded_orders(self):
 order_offsets=[]
```

```
 for k in range(len(self.orders)):
 if self.orders[k]['status'] == 'filled':
 order_offsets.append(k)
 if len(order_offsets):
 for k in sorted(order_offsets,reverse=True):
 del (self.orders[k])
```

Since the OrderManager component is critical for the safety of your trading, we need to have exhaustive unit testing to ensure that no strategy will damage your gain, and prevent you from incurring losses:

```
import unittest
from chapter7.OrderManager import OrderManager
class TestOrderBook(unittest.TestCase):
 def setUp(self):
 self.order_manager = OrderManager()
```

The test\_receive\_order\_from\_trading\_strategy test verifies whether an order is correctly received by the order manager. First, we create an order, order1, and we call the handle\_order\_from\_trading\_strategy function. Since the trading strategy creates two orders (stored in the channel ts\_2\_om), we call the test\_receive\_order\_from\_trading\_strategy function twice. The order manager will then generate two orders. In this example, since we only have one strategy, when the orders are created by the order manager, they will have the same order IDs as the trading strategy created:

```
 def test_receive_order_from_trading_strategy(self):
 order1 = {
 'id': 10,
 'price': 219,
 'quantity': 10,
 'side': 'bid',
 }
 self.order_manager.handle_order_from_trading_strategy(order1)
 self.assertEqual(len(self.order_manager.orders),1)
 self.order_manager.handle_order_from_trading_strategy(order1)
 self.assertEqual(len(self.order_manager.orders),2)
 self.assertEqual(self.order_manager.orders[0]['id'],1)
 self.assertEqual(self.order_manager.orders[1]['id'],2)
```

To prevent a malformed order from being sent to the market, the test\_receive\_order\_from\_trading\_strategy\_error test checks whether an order created with a negative price is rejected:

```
 def test_receive_order_from_trading_strategy_error(self):
 order1 = {
```

```
 'id': 10,
 'price': -219,
 'quantity': 10,
 'side': 'bid',
 }
 self.order_manager.handle_order_from_trading_strategy(order1)
 self.assertEqual(len(self.order_manager.orders),0)
```

The following test, test\_receive\_from\_gateway\_filled, confirms a market response has been propagated by the order manager:

```
 def test_receive_from_gateway_filled(self):
 self.test_receive_order_from_trading_strategy()
 orderexecution1 = {
 'id': 2,
 'price': 13,
 'quantity': 10,
 'side': 'bid',
 'status' : 'filled'
 }
 self.order_manager.handle_order_from_gateway(orderexecution1)
 self.assertEqual(len(self.order_manager.orders), 1)
 def test_receive_from_gateway_acked(self):
 self.test_receive_order_from_trading_strategy()
 orderexecution1 = {
 'id': 2,
 'price': 13,
 'quantity': 10,
 'side': 'bid',
 'status' : 'acked'
 }
 self.order_manager.handle_order_from_gateway(orderexecution1)
 self.assertEqual(len(self.order_manager.orders), 2)
 self.assertEqual(self.order_manager.orders[1]['status'], 'acked')
```

### **MarketSimulator class**

The MarketSimulator class is central in validating your trading strategy. You will use this class to fix the market assumptions. For instance, you can indicate the rejection rate and which type of orders can be accepted, and you can set the trading rules belonging to the exchange you are targeting. In our example, the market simulator acknowledges and fills all new orders.

When creating this class, the constructor will have two channels. One will get input from the order manager and the other will give the response back to the order manager:

```
class MarketSimulator:
 def __init__(self, om_2_gw=None,gw_2_om=None):
 self.orders = []
 self.om_2_gw = om_2_gw
 self.gw_2_om = gw_2_om
```

The lookup\_orders function will help to look up outstanding orders:

```
 def lookup_orders(self,order):
 count=0
 for o in self.orders:
 if o['id'] == order['id']:
 return o, count
 count+=1
 return None, None
```

The handle\_order\_from\_gw function will collect the order from the gateway (the order manager) through the om\_2\_gw channel:

```
 def handle_order_from_gw(self):
 if self.om_2_gw is not None:
 if len(self.om_2_gw)>0:
 self.handle_order(self.om_2_gw.popleft())
 else:
 print('simulation mode')
```

The trading rule that we use in the handle\_order function will accept any new orders. If an order already has the same order ID, the order will be dropped. If the order manager cancels or amends an order, the order is automatically

canceled and amended. The logic you will code in this function will be adapted to your trading:

```
 def handle_order(self, order):
 o,offset=self.lookup_orders(order)
 if o is None:
 if order['action'] == 'New':
 order['status'] = 'accepted'
 self.orders.append(order)
 if self.gw_2_om is not None:
 self.gw_2_om.append(order.copy())
 else:
 print('simulation mode')
 return
 elif order['action'] == 'Cancel' or order['action'] == 'Amend':
 print('Order id - not found - Rejection')
 if self.gw_2_om is not None:
 self.gw_2_om.append(order.copy())
 else:
 print('simulation mode')
 return
 elif o is not None:
 if order['action'] == 'New':
 print('Duplicate order id - Rejection')
 return
 elif order['action'] == 'Cancel':
 o['status']='cancelled'
 if self.gw_2_om is not None:
 self.gw_2_om.append(o.copy())
 else:
 print('simulation mode')
 del (self.orders[offset])
 print('Order cancelled')
 elif order['action'] == 'Amend':
 o['status'] = 'accepted'
 if self.gw_2_om is not None:
 self.gw_2_om.append(o.copy())
 else:
 print('simulation mode')
 print('Order amended')
 def fill_all_orders(self):
 orders_to_be_removed = []
 for index, order in enumerate(self.orders):
 order['status'] = 'filled'
 orders_to_be_removed.append(index)
 if self.gw_2_om is not None:
 self.gw_2_om.append(order.copy())
 else:
 print('simulation mode')
 for i in sorted(orders_to_be_removed,reverse=True):
 del(self.orders[i])
```

The unit test will ensure that the trading rules are verified:

**import** unittest **from** chapter7.MarketSimulator **import** MarketSimulator

```
class TestMarketSimulator(unittest.TestCase):
 def setUp(self):
 self.market_simulator = MarketSimulator()
 def test_accept_order(self):
 self.market_simulator
 order1 = {
 'id': 10,
 'price': 219,
 'quantity': 10,
 'side': 'bid',
 'action' : 'New'
 }
 self.market_simulator.handle_order(order1)
 self.assertEqual(len(self.market_simulator.orders),1)
 self.assertEqual(self.market_simulator.orders[0]['status'], 'accepted')
 def test_accept_order(self):
 self.market_simulator
 order1 = {
 'id': 10,
 'price': 219,
 'quantity': 10,
 'side': 'bid',
 'action' : 'Amend'
 }
 self.market_simulator.handle_order(order1)
 self.assertEqual(len(self.market_simulator.orders),0)
```

## **TestTradingSimulation class**

The goal of the TestTradingSimulation class is to create the full trading system by gathering all the prior critical components together.

This class checks whether, for a given input, we have the expected output. Additionally, we will test whether the PnL of the trading strategy has been updated accordingly.

We will first need to create all the deques representing the communication channels within the trading systems:

```
import unittest
from chapter7.LiquidityProvider import LiquidityProvider
from chapter7.TradingStrategy import TradingStrategy
from chapter7.MarketSimulator import MarketSimulator
from chapter7.OrderManager import OrderManager
from chapter7.OrderBook import OrderBook
from collections import deque
class TestTradingSimulation(unittest.TestCase):
 def setUp(self):
 self.lp_2_gateway=deque()
 self.ob_2_ts = deque()
 self.ts_2_om = deque()
 self.ms_2_om = deque()
 self.om_2_ts = deque()
 self.gw_2_om = deque()
 self.om_2_gw = deque()
```

We instantiate all the critical components of the trading system:

```
 self.lp=LiquidityProvider(self.lp_2_gateway)
 self.ob=OrderBook(self.lp_2_gateway, self.ob_2_ts)
 self.ts=TradingStrategy(self.ob_2_ts,self.ts_2_om,self.om_2_ts)
 self.ms=MarketSimulator(self.om_2_gw,self.gw_2_om)
 self.om=OrderManager(self.ts_2_om, self.om_2_ts,self.om_2_gw,self.gw_2_om)
```

We test whether. by adding two liquidities having a bid higher than the offer, we will create two orders to arbitrage these two liquidities. We will check whether the components function correctly by checking what they push to their respective channels. Finally, since we will buy 10 liquidities at a price of 218 and we sell at a price of 219, the PnL should be 10:

```
 def test_add_liquidity(self):
 # Order sent from the exchange to the trading system
 order1 = {
 'id': 1,
 'price': 219,
 'quantity': 10,
 'side': 'bid',
 'action': 'new'
 }
 self.lp.insert_manual_order(order1)
 self.assertEqual(len(self.lp_2_gateway),1)
 self.ob.handle_order_from_gateway()
 self.assertEqual(len(self.ob_2_ts), 1)
 self.ts.handle_input_from_bb()
 self.assertEqual(len(self.ts_2_om), 0)
 order2 = {
 'id': 2,
 'price': 218,
 'quantity': 10,
 'side': 'ask',
 'action': 'new'
 }
 self.lp.insert_manual_order(order2.copy())
 self.assertEqual(len(self.lp_2_gateway),1)
 self.ob.handle_order_from_gateway()
 self.assertEqual(len(self.ob_2_ts), 1)
 self.ts.handle_input_from_bb()
 self.assertEqual(len(self.ts_2_om), 2)
 self.om.handle_input_from_ts()
 self.assertEqual(len(self.ts_2_om), 1)
 self.assertEqual(len(self.om_2_gw), 1)
 self.om.handle_input_from_ts()
 self.assertEqual(len(self.ts_2_om), 0)
 self.assertEqual(len(self.om_2_gw), 2)
 self.ms.handle_order_from_gw()
 self.assertEqual(len(self.gw_2_om), 1)
 self.ms.handle_order_from_gw()
 self.assertEqual(len(self.gw_2_om), 2)
 self.om.handle_input_from_market()
 self.om.handle_input_from_market()
 self.assertEqual(len(self.om_2_ts), 2)
 self.ts.handle_response_from_om()
 self.assertEqual(self.ts.get_pnl(),0)
 self.ms.fill_all_orders()
 self.assertEqual(len(self.gw_2_om), 2)
 self.om.handle_input_from_market()
 self.om.handle_input_from_market()
 self.assertEqual(len(self.om_2_ts), 3)
 self.ts.handle_response_from_om()
 self.assertEqual(len(self.om_2_ts), 2)
 self.ts.handle_response_from_om()
 self.assertEqual(len(self.om_2_ts), 1)
 self.ts.handle_response_from_om()
 self.assertEqual(len(self.om_2_ts), 0)
 self.assertEqual(self.ts.get_pnl(),10)
```

## **Designing a limit order book**

A limit order book is a component that gathers all the orders and sorts them in a way that facilitates the work of the trading strategy. The order book is used by exchanges to maintain sell and buy orders. When we trade, we need to get the book of the exchange to know which prices are the best or just to have a view on the market. Because the exchange is located on another machine, we will need to use the network to communicate changes on the exchange book. For that, we have two methods:

- The first method is to send the whole book. You will realize that this method would be very slow, especially when the exchanges is as large as NYSE or NASDAQ. This solution is not scalable.
- The second method is to first send the whole book (like the first method), but then instead of sending the whole book each time there is an update, we just send the update. This update will be the order (from the other traders placing orders on the exchange). They will arrive by time increments as small as microseconds.

The trading strategy needs to make a decision very rapidly (buying, selling, or holding stocks). Since the book provides the required information to the trading strategies to make the decision, it needs to be fast. An order book is, in reality, a book for the orders coming from buyers and a book for the orders from sellers. The highest bid and the lowest offer prices will have priority. In a situation where there is more than one bid with the same price competing for the best price, the time stamp will be used to sort out which one should be sold. The timestamp that is the earliest will be executed first.

The operations we will need to handle for the life cycle of the orders are the following:

**Insertion**: An insertion will add an order to the book. This operation should be fast. The algorithm and data structure chosen for this operation are critical, because we need to have the book of bids and

offers sorted at any time. We will have to privilege a data structure allowing a complexity of O(1) or O(log n) to insert a new order.

- **Amendment/modification**: An amendment will look up the order in the book by using the order ID. This operation should also be with the same complexity as the insertion.
- **Cancelation**: A cancelation will allow an order to be removed from the book by using the order ID.

As you can understand, the choice of data structure and the algorithm associated with this data structure will change the performance a lot. If you are building a high-frequency trading system, you will need to choose accordingly. Since we are using Python and we are not implementing a high-frequency trading system, we will then use a list to simplify the coding part. This list will represent the orders and this list will be sorted for both sides (for the book of bids and for the book of offers).

We will build an OrderBook class*;* this class will collect orders from LiquidityProvider and sort the orders and create book events. The book events in a trading system are preset events and these events can be anything a trader thinks it is worth knowing. For instance, in this implementation, we choose to generate a book event each time there is a change on the top of the book (any changes in the first level of the book will create an event):

1. We choose to code OrderBook by having a list for *asks* and *bids*. The constructor has two optional arguments, which are the two channels to receive orders and send book events:

```
class OrderBook:
 def __init__(self,gt_2_ob = None,ob_to_ts = None):
 self.list_asks = []
 self.list_bids = []
 self.gw_2_ob=gt_2_ob
 self.ob_to_ts = ob_to_ts
 self.current_bid = None
 self.current_ask = None
```

2. We will write a function, handle\_order\_from\_gateway, which will receive the orders from the liquidity provider. Let's have a look at the code:

```
def handle_order_from_gateway(self,order = None):
 if self.gw_2_ob is None:
 print('simulation mode')
```

```
 self.handle_order(order)
 elif len(self.gw_2_ob)>0:
 order_from_gw=self.gw_2_ob.popleft()
 self.handle_order(order_from_gw)
```

3. Next, as shown, we will write a function to check whether the gw\_2\_ob channel has been defined. If the channel has been instantiated, handle\_order\_from\_gateway will pop the order from the top of deque gw\_2\_ob and will call the handle\_order function to process the order for a given action:

```
def handle_order(self,o):
 if o['action']=='new':
 self.handle_new(o)
 elif o['action']=='modify':
 self.handle_modify(o)
 elif o['action']=='delete':
 self.handle_delete(o)
 else:
 print('Error-Cannot handle this action')
 return self.check_generate_top_of_book_event()
```

In the code, handle\_order calls either handle\_modify, handle\_delete, or handle\_new.

The handle\_modify function modifies the order from the book by using the order given as an argument of this function.

The handle\_delete function removes an order from the book by using the order given as an argument of this function.

The handle\_new function adds an order to the appropriate

list, self.list\_bids and self.list\_asks .

The code shows the implementation of the insertion of a new order. In this code, we check the order side. Depending on the side, we will choose the list of the bids or the list of asks:

```
 if o['side']=='bid':
 self.list_bids.append(o)
 self.list_bids.sort(key=lambda x: x['price'],reverse=True)
 elif o['side']=='ask':
 self.list_asks.append(o)
 self.list_asks.sort(key=lambda x: x['price'])
```

4. As shown in the code, we will then implement the handle\_modify function to manage the amendment. This function searches in the list of orders if the order exists. If that's the case, we will modify the quantity by the new quantity. This operation will be possible only if we reduce the quantity of the order:

```
def handle_modify(self,o):
 order=self.find_order_in_a_list(o)
 if order['quantity'] > o['quantity']:
 order['quantity'] = o['quantity']
 else:
 print('incorrect size')
 return None
```

5. The handle\_delete function will manage the order cancelation. As shown in the code, we will remove the orders from the list of orders by checking whether the order exists with the order ID:

```
def handle_delete(self,o):
 lookup_list = self.get_list(o)
 order = self.find_order_in_a_list(o,lookup_list)
 if order is not None:
 lookup_list.remove(order)
 return None
```

The following two functions will help with finding an order by using the order ID.

6. The get\_list function in the code will help to find the side (which order book) contains the order:

```
def get_list(self,o):
 if 'side' in o:
 if o['side']=='bid':
 lookup_list = self.list_bids
 elif o['side'] == 'ask':
 lookup_list = self.list_asks
 else:
 print('incorrect side')
 return None
 return lookup_list
 else:
 for order in self.list_bids:
 if order['id']==o['id']:
 return self.list_bids
 for order in self.list_asks:
 if order['id'] == o['id']:
 return self.list_asks
 return None
```

7. The find\_order\_in\_a\_list function will return a reference to the order if this order exists:

```
 def find_order_in_a_list(self,o,lookup_list = None):
 if lookup_list is None:
 lookup_list = self.get_list(o)
 if lookup_list is not None:
 for order in lookup_list:
 if order['id'] == o['id']:
 return order
 print('order not found id=%d' % (o['id']))
 return None
```

The following two functions will help with creating the book events. The book events as defined in the

check\_generate\_top\_of\_book\_event function will be created by having the top of the book changed.

8. As shown, the create\_book\_event function creates a dictionary representing a book event. In this example, a book event will be given to the trading strategy to indicate what change was made at the top of the book level:

```
def create_book_event(self,bid,offer):
 book_event = {
 "bid_price": bid['price'] if bid else -1,
 "bid_quantity": bid['quantity'] if bid else -1,
 "offer_price": offer['price'] if offer else -1,
 "offer_quantity": offer['quantity'] if offer else -1
 }
 return book_event
```

9. As shown, the check\_generate\_top\_of\_book\_event function will create a book event when the top of the book has changed. When the price or the quantity for the best bid or offer has changed, we will inform the trading strategies that there is a change at the top of the book:

```
def check_generate_top_of_book_event(self):
 tob_changed = False
 if not self.list_bids:
 if self.current_bid is not None:
 tob_changed = True
 # if top of book change generate an event
 if not self.current_bid:
 if self.current_bid != self.list_bids[0]:
 tob_changed=True
 self.current_bid=self.list_bids[0] \
 if self.list_bids else None
```

```
 if not self.current_ask:
 if not self.list_asks:
 if self.current_ask is not None:
 tob_changed = True
 elif self.current_ask != self.list_asks[0]:
 tob_changed = True
 self.current_ask = self.list_asks[0] \
 if self.list_asks else None
 if tob_changed:
 be=self.create_book_event(self.current_bid,self.current_ask)
 if self.ob_to_ts is not None:
 self.ob_to_ts.append(be)
 else:
 return be
```

When we test the order book, we need to test the following functionalities:

- Adding a new order
- Modifying a new order
- Deleting an order
- Creating a book event

This code will start creating the unit test for the Order Book. We will use the function setUp called for every test cases and create an reference to the Order Book for all the test cases.

```
import unittest
from chapter7.OrderBook import OrderBook
class TestOrderBook(unittest.TestCase):
 def setUp(self):
 self.reforderbook = OrderBook()
```

10. We will create a function to verify if the order insertion works. The book must have the list of asks and the list of bids sorted:

```
 def test_handlenew(self):
 order1 = {
 'id': 1,
 'price': 219,
 'quantity': 10,
 'side': 'bid',
 'action': 'new'
 }
 ob_for_aapl = self.reforderbook
 ob_for_aapl.handle_order(order1)
 order2 = order1.copy()
```

```
 order2['id'] = 2
 order2['price'] = 220
 ob_for_aapl.handle_order(order2)
 order3 = order1.copy()
 order3['price'] = 223
 order3['id'] = 3
 ob_for_aapl.handle_order(order3)
 order4 = order1.copy()
 order4['side'] = 'ask'
 order4['price'] = 220
 order4['id'] = 4
 ob_for_aapl.handle_order(order4)
 order5 = order4.copy()
 order5['price'] = 223
 order5['id'] = 5
 ob_for_aapl.handle_order(order5)
 order6 = order4.copy()
 order6['price'] = 221
 order6['id'] = 6
 ob_for_aapl.handle_order(order6)
 self.assertEqual(ob_for_aapl.list_bids[0]['id'],3)
 self.assertEqual(ob_for_aapl.list_bids[1]['id'], 2)
 self.assertEqual(ob_for_aapl.list_bids[2]['id'], 1)
 self.assertEqual(ob_for_aapl.list_asks[0]['id'],4)
 self.assertEqual(ob_for_aapl.list_asks[1]['id'], 6)
 self.assertEqual(ob_for_aapl.list_asks[2]['id'], 5)
```

11. Next, we will write the following function to test whether the amendment works. We fill the book by using the prior function, then we amend the order by changing the quantity:

```
 def test_handleamend(self):
 self.test_handlenew()
 order1 = {
 'id': 1,
 'quantity': 5,
 'action': 'modify'
 }
 self.reforderbook.handle_order(order1)
 self.assertEqual(self.reforderbook.list_bids[2]['id'], 1)
 self.assertEqual(self.reforderbook.list_bids[2]['quantity'], 5)
```

12. The last function in the code involves book management that removes order from the book by the order ID. In this test case, we fill the book with the prior function and we remove the order:

```
 def test_handledelete(self):
 self.test_handlenew()
 order1 = {
 'id': 1,
 'action': 'delete'
 }
 self.assertEqual(len(self.reforderbook.list_bids), 3)
```

```
 self.reforderbook.handle_order(order1)
 self.assertEqual(len(self.reforderbook.list_bids), 2)
```

13. The book event is created when there is a change at the top of the book. We will write the following function to test the creation of the book event after the top of the book changes:

```
 def test_generate_book_event(self):
 order1 = {
 'id': 1,
 'price': 219,
 'quantity': 10,
 'side': 'bid',
 'action': 'new'
 } 
 ob_for_aapl = self.reforderbook
 self.assertEqual(ob_for_aapl.handle_order(order1),
 {'bid_price': 219, 'bid_quantity': 10,
 'offer_price': -1, 'offer_quantity': -1})
 order2 = order1.copy()
 order2['id'] = 2
 order2['price'] = 220
 order2['side'] = 'ask'
 self.assertEqual(ob_for_aapl.handle_order(order2),
 {'bid_price': 219, 'bid_quantity': 10,
 'offer_price': 220, 'offer_quantity': 10})
 if __name__ == '__main__':
 unittest.main()
```

In this section, we studied how to build a limit order book. This was a naive implementation. The complexity to add an order is in the order of *O(N)* and for each insertion, we use a sorting algorithm with a complexity of *O(N log N)*. In order to get a book working faster for order insertion, order lookup, we should use more advanced data structures, as described in *Algorithm Analysis, Packt Publishing*. Because we need to sort the order by price, we need to use an ordered data structure, such as trees. We will change the complexity of insertion to *O(log N)*. Concurrently, we will fix the lookup time to retrieve the best price.

## **Summary**

In this chapter, we learned how to build a Python trading system. The trading system we built presents the critical components that you will need to start trading in real time. Depending on the trading strategy you implement, you will add some services and you will modify the behavior of these components. As mentioned at the beginning of this chapter, the number of traders, the type of strategies, and the types of asset classes will affect the design of the trading system. Learning how to design a trading system takes years and it is very common to become expert in a trading system for a given strategy, given asset class and given number of users. But it is uncommon to become expert in all trading system types because of their complexity. We built the minimum functionalities that a trading system must have. To be fully functional, we need to learn how to get this component connected to a trading system.

In the next chapter, we will focus on explaining all the details related to connection with exchanges.

# **Connecting to Trading Exchanges**

At this point, we have a good understanding of how to write a trading system and writing the code for all the critical components. We went into detail about book building, creating trading signals, and getting a market response.

In this chapter, we will introduce the component that's in charge of communicating with the outside world and the gateway. We will look at the different functionalities of this component and describe the different types of protocols that we will encounter. Finally, we will implement a gateway that will connect to a real liquidity provider.

In this chapter, we will cover the following topics:

- Making a trading system trade with exchanges
- Reviewing the Communication API
- Receiving price updates
- Sending orders and receiving market responses

# **Making a trading system trade with exchanges**

As we saw in Chapter 7, *Building a Trading System in Python*, a trading system is a piece of software that is capable of collecting financial data and sending orders to the market. This trading system has many functional components that are in charge of handling trading and risks, as well as monitoring the trading process that happens on one or many exchanges. When you code a trading strategy, it will become a component of the trading system. You will need input price information and your trading strategy as output. This will send trading indications. To complete this flow, we require gateways since they are the main components.

The following diagram shows the functional components of a trading system, the gateway's interface, and the outside world with the trading system. The gateways collect prices and market responses and send orders. Its main role is to initiate a connection and to convert the data that's sent from the outside world into the data structure that will be used in the trading system:

![](_page_49_Figure_0.jpeg)

The following is shown in the preceding diagram:

- When you implement your trading strategy, this trading strategy will be on your machine. The exchange will be located on another machine.
- Since these two machines are on different sites, they need to communicate through a network.
- Depending on the location of the system, the ways that are used to communicate can be different.
- If the trading system is collocated (the machines are located in the same facility), a single wire will be used, which will reduce the network latency.
- If we use a cloud solution, the internet could be another method of communication. In that case, the communication will be much slower than a direct connect one.

Take a look at the following diagram, which depicts the communication taking place between the gateways:

![](_page_50_Figure_0.jpeg)

The following is shown in the preceding diagram:

- When we look closer at the communication that's handled by the gateways, we can observe that the venues can have different protocols.
- The gateways will need to be able to process numerous protocols so that they can convert them into trading system data structures.

# **Reviewing the Communication API**

Network protocols define the rules of communication between machines. They define how these machines will be recognized on the network and how they will interact. In trading finance, we use the UDP and TCP over the IP protocol. Additionally, we use a software protocol that will define how to communicate with an order and get a price update. The Communication API will set the rules of communication at the software level. The Communication API is given by the entity that you would like to trade with. This document contains all the messages that you will use to receive prices and send orders.

[You can find examples of trading API documents at](https://en.wikipedia.org/wiki/List_of_electronic_trading_protocols) https://en.wikipedia.org/w iki/List\_of\_electronic\_trading\_protocols.

Before diving into the trading API, we will need to explain the basics of networking.

## **Network basics**

The network is in charge of making the computers communicate with each other. Networks need a physical layer to share information. Choosing the correct media (communication layer) is critical for the network to reach a given speed or reliability, or even security. In trading finance, we use the following:

- **Wire**: Electrical currents that are limited in bandwidth
- **Fiber**: More bandwidth
- **Microwave**: An easy-to-install, large bandwidth, but can be impacted by storms

The media will vary, depending on the type of trading strategy you're using. Choosing the correct media is part of the first layer of the network in the ISO model. This layer is called the physical layer. On top of this one, there are six more layers describing the type of communication. The protocol that we will be using in trading finance is the IP protocol. This is a part of the network layer of the ISO model. This IP protocol sets the rules for routing network packets in the network. The last layer that we will talk about is the transport layer. The two most well-known protocols in finance are TCP and UDP. These two protocols are very different. TCP works by establishing communication between two machines. All the messages that were sent first will arrive first. UDP doesn't have any mechanism to establish whether the network packets have been received by the network.

All the exchanges will choose their own protocol by using either TCP or UDP. In the next section, we will talk about the content that's sent through the network.

#### **Trading protocols**

To have two entities communicate with each other, they need to talk the same language. In networking, we use a protocol. In trading, this protocol is used for any venue. Some venues can have numerous protocols. Even if they are different, the steps that these protocols go through to establish a connection and start trading are similar:

- 1. They start by initiating a logon describing who the trading initiator is, who the recipient is, and how the communication remains alive.
- 2. Then, they inquire about what they expect from the different entities, for example, trading or subscribing price updates.
- 3. After, that they receive orders and price updates.
- 4. Then, they maintain communication by sending heartbeats.
- 5. Finally, they close communication.

The protocol we will be using in this chapter is called the **Financial Information eXchange** (**FIX**) protocol. It was created in 1992 for international real-time exchanges to handle securities between Fidelity Investments and Salomon Brothers. It expanded to **foreign exchange** (**FX**), **fixed income** (**FI**), derivatives, and clearing. This protocol is a string-based protocol, which means humans can read it. It is platform-independent, is an open protocol, and has many versions. The most widely used versions are versions 4.2, 4.4, 5, and 1. There are two types of messages:

- The administrative messages, which do not carry any financial data
- The application messages, which are used to get price updates and orders

The content of these messages is like a Python dictionary: it is a list of key-value pairs. The keys are predefined tags; every tag is a number that corresponds to a specific feature. Associated with these tags are the values, which can be numerical or string values. Let's take a look at an example:

- Let's say that the tag corresponding to the price of an order has the value 44 if we want to send an order with a price of \$1.23. Therefore, in the order message, we will have 44=1.23.
- All the pairs are character-1 separated. This means that if we add the quantity (tag 38) of 100,000 to our prior example to create an order, we will have 44=1.23|38=100000. The| symbol represents the character-1.

- All the messages start with a prefix, that is, 8=FIX.X.Y. This prefix indicates the fix version numbers. X and Y represent the numbers of the version.
- They all terminate when 10=nn corresponds to the checksum.
- The checksum is the sum of all the binary values in the message. It helps us identify transmission problems.

The following is an example of an FIX message:

8=FIX.4.2|9=76|35=A|34=1|49=DONALD|52=20160617-23:11:55.884|56=VENUE1|98=0|108=30|141=Y|10=134

The preceding FIX message has the following mandatory fields:

- A tag of 8, which is associated with the value 4.2. This corresponds to the FIX version number.
- A version number lower than FIX4.4: 8(BeginString), 9(BodyLength), and 35(MsgType).
- A version number higher than FIX4.4: 8(BeginString), 9(BodyLength), 35(MsgType), 49(SnderCompID), and 56(TargetCompID).
- The message type is defined by the tag 35.
- The body length tag, 9, corresponds to the character count starting at tag 35 all the way to tag 10.
- The 10 field is the checksum. The value is calculated by summing up the decimal value of the ASCII representation of all the bytes up to, but not including, the checksum field (which is the last field), and returns the value modulo 256.

## **FIX communication protocols**

A trading system must use two connections to be able to trade: one connection to receive the price updates, and another one for the orders. The FIX protocol conforms to that requirement by having different messages for the following connections.

# **Price updates**

Trading systems need prices for the liquidities that traders choose to trade. For that, it initiates a connection to the exchange to subscribe to liquidity updates.

The following diagram describes the communication between the initiator, which is the trading system, and the acceptor, which is the exchange:

![](_page_56_Figure_3.jpeg)

The following diagram represents the FIX messages that are exchanged between the acceptor and the initiator:

![](_page_57_Figure_0.jpeg)

Upon reception of these price updates, the trading system updates the books and will place orders based on a given signal.

## **Orders**

The trading system will communicate the orders to the exchange by opening a trading session with the exchange. While this active trading session stays open, order messages will be sent to the exchange. The exchange will communicate the state of these orders by using FIX messages. This is shown in the following diagram:

![](_page_58_Figure_2.jpeg)

The following diagram represents the FIX messages that are exchanged between the initiator and the acceptor:

|                        | 8=FIX.4.2 9=76 35=A 34=1 49=DONALD 52=20160617-23:11:55.884 56=VENUE1 98=0 108=30 141=Y 10=134 <br>8=FIX.4.2 9=76 35=A 34=1 49=VENUE 52=20160617-23:11:55.886 56=DONALD 98=0 108=30 141=Y 10=136                                                                                                                                                                                                                                                                                       |                       |
|------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------|
|                        | 8=FIX.4.2 9=124 35=D 34=2 49=DONALD 52=20160613-22:52:37.227 56=VENUE <br>11=1 21=3 38=3 40=2 44=100 54=1 55=MQ 60=20160613-22:52:37.227 10=163                                                                                                                                                                                                                                                                                                                                        |                       |
| Exchange<br>(acceptor) | 8=FIX.4.2 9=140 35=8 34=2 49=VENUE 52=20160613-22:52:37.228 56=DONALD 6=10 <br>11=1 14=100 17=1 20=0 31=10 32=100 37=1 38=3 39=0 54=1 55=MQ 150=0 151=0 10=184                                                                                                                                                                                                                                                                                                                         |                       |
|                        | 8=FIX.4.2  9=140   35=8   34=2   49=VENUE   52=20160613-22:52:37.228   56=DONALD  <br>$6=10\begin{vmatrix} 11=1 \end{vmatrix} 14=100\begin{vmatrix} 17=1 \end{vmatrix} 20=0\begin{vmatrix} 31=10 \end{vmatrix} 32=100\begin{vmatrix} 37=1 \end{vmatrix} 38=3\begin{vmatrix} 39=2 \end{vmatrix} 54=1\begin{vmatrix} 55=\text{MQ} \end{vmatrix} 150=2\begin{vmatrix} 151=0 \end{vmatrix} 10=184\begin{vmatrix} 150=2 \end{vmatrix} 151=0\begin{vmatrix} 10=184 \end{vmatrix} 150=2\$<br> | System<br>(initiator) |
|                        | 8=FIX.4.2  9=54  35=5‡34=20‡49=DONALD  52=20160617-23:12:01.33  56=VENUE  10=134                                                                                                                                                                                                                                                                                                                                                                                                       |                       |
|                        | 8=FIX.4.2  9=54  35=5‡34=20‡49=VENUE  52=20160617-23:12:05.55  56=DONALD  10=134                                                                                                                                                                                                                                                                                                                                                                                                       |                       |

## **Receiving price updates**

When we implement an FIX parser and an FIX composer, we know how tedious and time-consuming this process is. If you choose to implement these parts from scratch, you will need to take care of the network connections, the parsing operations, and the part creating the FIX messages. Because we want to focus on creating a trading system that's capable of working quickly, we will want to use a library where all the functions have already been implemented. There are many commercial FIX libraries available, including NYFIX, Aegisfot – Aethna, Reuters – Traid, and Financial Fusion – Trade Force. The one we will use is called the quickfix library.

This library can be downloaded from <http://www.quickfixengine.org/>.

This library was created in 2000 and is supported by Java, C++, and Python.

The libraries simplify the developer's role by using callbacks. A callback is a computer engineering term and something that we will be using if we have a task that could take some time to finish. In naive code (code without callbacks), we wait for the end of the execution of this task.

If we use a callback system, the following takes place:

- We start a task and then proceed to the other tasks while this task keeps running.
- Once that task has finished, it will call a function to leave the program to handle the result of this task. Let's assume that we have a trading system with many tasks.
- If one of them is to receive price updates from exchanges, we just use a callback that's triggered once a price update has been received and parsed by the system.
- Once the callback has been called, we will be able to read the specific fields we need in order to proceed with the rest of our system by using

this new price update.

The quickfix library gives the developer the ability to implement specific tasks for any messages that are received by the trading system. The following code describes the general structure of a piece of Python code using the quickfix library:

```
import sys
import time
import quickfix as fix
import quickfix42 as fix42
class Application(fix.Application):
 def onCreate(self, sessionID): return
 def onLogon(self, sessionID):
 self.sessionID = sessionID
 print ("Successful Logon to session '%s'." % sessionID.toString())
 return
 def onLogout(self, sessionID): return
 def toAdmin(self, sessionID, message):return
 def fromAdmin(self, sessionID, message):return
 def toApp(self, sessionID, message):
 print "Sent the following message: %s" % message.toString()
 return
 def fromApp(self, message, sessionID):
 print "Received the following message: %s" % message.toString()
 return
```

The code imports the quickfix library and creates a

class called Application that's derived from the fix.Application object. Let's go through this now:

- The onLogon and onLogout functions are callback functions that are called when a logon/logout message (35=A) has been received and parsed by the system. The argument of the onLogon function is the session ID. It is received when a connection has been successfully established between the acceptor and the initiator.
- The onCreate function is called when a new session is created to initialize a trading session.
- The toAdmin and toApp functions are used to modify the messages that are sent to the acceptor.
- The fromAdmin and fromApp functions are called when we receive a message from the acceptor.
- The incoming code is the minimal code you need to have an FIX application in Python.

Each FIX application has its own config file. By reading the documentation on the quickfix library, you will learn how to configure the application. We are going to comment on a simple configuration example. The quickfix configuration file is divided into several parts. The DEFAULT part configures the main app attributes:

- The connection type: *Initiator* or *acceptor*
- The reconnection time: 60 seconds (in this config file)
- SenderCompIT: The identification of the initiator

The SESSION part describes the FIX message format. In this example, the FIX version that's being used is version 4.1. TargetCompID corresponding to the identification of the acceptor is ARCA. The heartbeat interval is set in this file. This sets a heartbeat that checks whether the acceptor is still alive and has been sent. The network connection is established by using a socket. This socket is created based on the IP address (SocketConnectHost) and the port (SocketConnectPort).

We use a dictionary that defines all the mandatory and optional tags for all the message types:

```
# default settings for sessions
[DEFAULT]
ConnectionType=initiator
ReconnectInterval=60
SenderCompID=TW
# session definition
[SESSION]
# inherit ConnectionType, ReconnectInterval and SenderCompID from default
BeginString=FIX.4.1
TargetCompID=ARCA
StartTime=12:30:00
EndTime=23:30:00
HeartBtInt=20
SocketConnectPort=9823
SocketConnectHost=123.123.123.123
DataDictionary=somewhere/FIX41.xml
```

For the upcoming code example, we will use some free open source software code from GitHub. It can be found at https://github.com/gloryofrobot s/fixsim[. This code is a good example of Python code for initiators and](https://github.com/gloryofrobots/fixsim) acceptors in terms of the price update and order side of things.

# **Initiator code example**

The initiator starts communication with the exchange. An initiator will take care of getting the price updates, while another initiator will take care of the order.

#### **Price updates**

The role of the initiator is to start a connection with the acceptor. When the connection is established, the initiator will subscribe to the acceptor and request price updates. The first function we will review is the function to subscribe. This function will be called once the connection is established.

The subscribe function will be called after fixed intervals. When this function is called, we need to check whether there is an active session. It will build the market data request by iterating through the list of symbols. Let's have a look at the following code block:

8=FIX.4.4|9=78|35=V|146=1|55=USD/RUB|460=4|167=FOR|262=2|263=1|264=0|265=0|267=2|269=0|269=0|10=222|

As we can see, the message will have a message type of 35=V. The tags and their corresponding fields and values have been listed in the following table:

| Tag | Field                   | Value   |
|-----|-------------------------|---------|
| 8   | BeginString             | FIX.4.4 |
| 9   | BodyLength              | 78      |
| 35  | MsgType                 | V       |
| 146 | NoRelatedSym            | 1       |
| 55  | Symbol                  | USD/RUB |
| 460 | Product                 | 4       |
| 167 | SecurityType            | FOR     |
| 262 | MDReqID                 | 2       |
| 263 | SubscriptionRequestType | 1       |
| 264 | MarketDepth             | 0       |
| 265 | MDUpdateType            | 0       |

| 267 | NoMDEntryTypes | 2   |
|-----|----------------|-----|
| 269 | MDEntryType    | 0   |
| 269 | MDEntryType    | 1   |
| 10  | CheckSum       | 222 |

We can see the following in the preceding table:

- For each symbol (the ticker you would like to trade), this function will create a new market data request message.
- Each market data request must have a unique identifier (Market Data Request ID, that is, MDReqID) that's associated with a given symbol. In the following example, we use USD/RUB:

```
def subscribe(self):
 if self.marketSession is None:
 self.logger.info("FIXSIM-CLIENT Market session is none, skip subscribing")
 return
 for subscription in self.subscriptions:
 message = self.fixVersion.MarketDataRequest()
 message.setField(quickfix.MDReqID(self.idGen.reqID()))
 message.setField(quickfix.SubscriptionRequestType(quickfix.SubscriptionRequestType_SNAPSHOT_PLUS_UPDATES))
 message.setField(quickfix.MDUpdateType(quickfix.MDUpdateType_FULL_REFRESH))
 message.setField(quickfix.MarketDepth(0))
 message.setField(quickfix.MDReqID(self.idGen.reqID()))
 relatedSym = self.fixVersion.MarketDataRequest.NoRelatedSym()
 relatedSym.setField(quickfix.Product(quickfix.Product_CURRENCY))
 relatedSym.setField(quickfix.SecurityType(quickfix.SecurityType_FOREIGN_EXCHANGE_CONTRACT))
 relatedSym.setField(quickfix.Symbol(subscription.symbol))
 message.addGroup(relatedSym)
 group = self.fixVersion.MarketDataRequest.NoMDEntryTypes()
 group.setField(quickfix.MDEntryType(quickfix.MDEntryType_BID))
 message.addGroup(group)
 group.setField(quickfix.MDEntryType(quickfix.MDEntryType_OFFER))
 message.addGroup(group)
 self.sendToTarget(message, self.marketSession)
```

We can see the following in the preceding code:

- Once we subscribe to all the desired symbols (in this example, currency pairs), the acceptor will start sending market updates.
- The onMarketDataSnapshotFullRefresh function will receive the full snapshot of every price update coming into the system.

The type of message that's received by the price update gateway is as follows:

8=FIX.4.4|9=429|35=W|34=1781|49=FIXSIM-SERVER-MKD|52=20190909-19:31:48.011|56=FIXSIM-CLIENT-MKD|55=EUR/USD|262=74|268=4|269=0|2

This function is a callback. It is called when a Full Snapshot message is received and parsed. The message parameter will contain the message. Let's have a look at the code:

```
def onMarketDataSnapshotFullRefresh(self, message, sessionID):
 fix_symbol = quickfix.Symbol()
 message.getField(fix_symbol)
```

```
 symbol = fix_symbol.getValue()
 group = self.fixVersion.MarketDataSnapshotFullRefresh.NoMDEntries()
 fix_no_entries = quickfix.NoMDEntries()
 message.getField(fix_no_entries)
 no_entries = fix_no_entries.getValue()
 for i in range(1, no_entries + 1):
 message.getGroup(i, group)
 price = quickfix.MDEntryPx()
 size = quickfix.MDEntrySize()
 currency = quickfix.Currency()
 quote_id = quickfix.QuoteEntryID()
 group.getField(quote_id)
 group.getField(currency)
 group.getField(price)
 group.getField(size)
 quote = Quote()
 quote.price = price.getValue()
 quote.size = size.getValue()
 quote.currency = currency.getValue()
 quote.id = quote_id.getValue()
 fix_entry_type = quickfix.MDEntryType()
 group.getField(fix_entry_type)
 entry_type = fix_entry_type.getValue()
```

As we can see, we can access the field by using the getField method.

#### **Sending orders and receiving a market response**

The main goal of a trading system is to send orders and receive market responses regarding these orders. In this section, we will cover how to send an order and how to get an update on these orders.

The role of the initiator is to initiate a connection with the acceptor. When the connection is established, the trading session is enabled. From this very moment, the trading system can send orders to the exchange. The order will have the following type of message:

8=FIX.4.4|9=155|35=D|11=3440|15=USD|21=2|38=20000|40=D|44=55.945|54=1|55=USD/RUB|59=3|60=20190909-19:35:27|64=SP|107=SPOT|117=b

The initiator creates the orders by using the message type 35=D (representing a single order). All the fields of these orders will be filled in by the function of the quickfix library. Let's have a look at the code:

```
def makeOrder(self, snapshot):
 self.logger.info("FIXSIM-CLIENT Snapshot received %s", str(snapshot))
 quote = snapshot.getRandomQuote()
 self.logger.info("FIXSIM-CLIENT make order for quote %s", str(quote))
 order = self.fixVersion.NewOrderSingle()
 order.setField(quickfix.HandlInst(quickfix.HandlInst_AUTOMATED_EXECUTION_ORDER_PUBLIC_BROKER_INTERVENTION_OK))
 order.setField(quickfix.SecurityType(quickfix.SecurityType_FOREIGN_EXCHANGE_CONTRACT))
 order.setField(quickfix.OrdType(quickfix.OrdType_PREVIOUSLY_QUOTED))
 order.setField(quickfix.ClOrdID(self.idGen.orderID()))
 order.setField(quickfix.QuoteID(quote.id))
 order.setField(quickfix.SecurityDesc("SPOT"))
 order.setField(quickfix.Symbol(snapshot.symbol))
 order.setField(quickfix.Currency(quote.currency))
 order.setField(quickfix.Side(quote.side))
 order.setField(quickfix.OrderQty(quote.size))
 order.setField(quickfix.FutSettDate("SP"))
 order.setField(quickfix.Price(quote.price))
 order.setField(quickfix.TransactTime())
 order.setField(quickfix.TimeInForce(quickfix.TimeInForce_IMMEDIATE_OR_CANCEL))
```

Once an order is received by an exchange, it will be handled and the exchange will reply to this order with a specific FIX message. The nature of this message is the execution report 35=8.

The message will acknowledge the order by using the execution report message 35=8, the ExecType tag 150=0, and OrdStatus 39=0:

8=FIX.4.4|9=204|35=8|34=4004|49=FIXSIM-SERVER|52=20190909-19:35:27.085|56=FIXSIM-CLIENT|6=55.945|11=3440|14=20000|15=USD|17=344

The order will be filled and the server will send an execution report message indicating that 150=2 and 39=2 for a fill:

8=FIX.4.4|9=204|35=8|34=4005|49=FIXSIM-SERVER|52=20190909-19:35:27.985|56=FIXSIM-CLIENT|6=55.945|11=3440|14=20000|15=USD|17=344

The onExecutionReport callback in the code will be called once these messages are received by the trading system:

```
def onExecutionReport(self, connectionHandler, msg):
 codec = connectionHandler.codec
 if codec.protocol.fixtags.ExecType in msg:
 if msg.getField(codec.protocol.fixtags.ExecType) == "0":
 side = Side(int(msg.getField(codec.protocol.fixtags.Side)))
 logging.debug("<--- [%s] %s: %s %s %s@%s" % (codec.protocol.msgtype.msgTypeToName(msg.getField(codec.protocol.fixta
 elif msg.getField(codec.protocol.fixtags.ExecType) == "2":
 logging.info("Order Filled")
 else:
 logging.error("Received execution report without ExecType")
```

As shown in the preceding code, we have parsed the fields that we need to get the required information from the execution report message. We have also tested whether the order has been acknowledged or filled.

## **Acceptor code example**

The role of the acceptor is to receive the connection from the initiator. As an automatic trader, you will rarely code this part. However, you will be improving your knowledge if you know how exchange handle messages are sent by the initiator.

There are two main functions that an acceptor will take care of:

- **Market data request handling**: This is the function that's called when the market data request is received by the server.
- **Order handling**: This is the function that's called when order messages are received.

#### **Market Data request handling**

Market Data request handling allows the acceptor (the exchange) to register the request from an initiator who's willing to trade a given symbol. Once this request is received, the acceptor starts streaming the price updates to the initiator. Let's have a look at the following code:

```
def onMarketDataRequest(self, message, sessionID):
 requestID = quickfix.MDReqID()
 try:
 message.getField(requestID)
 except Exception as e:
 raise quickfix.IncorrectTagValue(requestID)
 try:
 relatedSym = self.fixVersion.MarketDataRequest.NoRelatedSym()
 symbolFix = quickfix.Symbol()
 product = quickfix.Product()
 message.getGroup(1, relatedSym)
 relatedSym.getField(symbolFix)
 relatedSym.getField(product)
 if product.getValue() != quickfix.Product_CURRENCY:
 self.sendMarketDataReject(requestID, " product.getValue() != quickfix.Product_CURRENCY:", sessionID)
 return
 # bid
 entryType = self.fixVersion.MarketDataRequest.NoMDEntryTypes()
 message.getGroup(1, entryType)
 # ask
 message.getGroup(2, entryType)
 symbol = symbolFix.getValue()
 subscription = self.subscriptions.get(symbol)
 if subscription is None:
 self.sendMarketDataReject(requestID, "Unknown symbol: %s" % str(symbol), sessionID)
 return
 subscription.addSession(sessionID)
 except Exception as e:
 print e,e.args
 self.sendMarketDataReject(requestID, str(e), sessionID)
```

As shown in the preceding code, the onMarketDataRequest callback that's handling the market data request does the following:

- **Gets the request ID**: The exchange will check whether the request ID has not already been processed.
- **Gets the symbol ID**: The symbol updates that are linked to this symbol will be sent to the initiator.
- **Gets the product**: The exchange checks whether the product that was requested is in the system. If the product isn't, a rejection message will be sent to the initiator.

#### **Order**

Order management is the main functionality of an initiator. An exchange must be capable of handling the following:

- **New order (35=D)**: This message is sent for a trading indication. This message can describe numerous types of orders, such as Limit, Fill or Kill, and Market order.
- **Cancel order (35=F)**: This message is sent to indicate that an order's been canceled.
- **Amend order (35=G)**: This message is sent to amend an order.

The onNewOrderSingle function is the function that handles the orders that are sent by the initiator. This function needs to get the principal order features:

- Symbol (the ticker symbol)
- Side (buy or sell)
- Type (market, limit, stop, stop limit, and so on)
- Quantity (the quantity to be traded)
- Price (the price to be traded)
- Client order ID (the unique identifier for an order)
- Quote ID (the quote identifier to be traded)

An exchange checks whether the order ID already exists. If it does, a rejection message should be sent to indicate that it isn't possible to create a new order with the same order ID. If the order is correctly received by the exchange, an execution report message will be sent to the initiator, indicating that the exchange has received the order.

In the GitHub fixsim code, the author chose to reject randomly incoming orders. When we will talk about backtesting later in this book, we will mention the different options we can introduce to model the market's behavior. Introducing a random rejection is one way of mimicking the market's behavior. If there is no rejection, the exchange will fill the order by sending an execution report 35=8 with an order status indicating that it's been filled.

The onNewOrderSingle function (callback) is divided into two parts. The first part collects the information from the *New Order* (35=D) message. The second part creates a response for the initiator. This response will be an *Execution Report* 35=8 message.

The code will create quickfix objects (symbol, side, ordType, and so on) and get the value from the tag values by using the getField function. The author of this code chooses to accept an order, but only if this order has been previously quoted. This means that the order will be based on a price update that has been received by our trading system:

```
def onNewOrderSingle(self, message, beginString, sessionID):
 symbol = quickfix.Symbol()
 side = quickfix.Side()
```

```
 ordType = quickfix.OrdType()
 orderQty = quickfix.OrderQty()
 price = quickfix.Price()
 clOrdID = quickfix.ClOrdID()
 quoteID = quickfix.QuoteID()
 currency = quickfix.Currency()
 message.getField(ordType)
 if ordType.getValue() != quickfix.OrdType_PREVIOUSLY_QUOTED:
 raise quickfix.IncorrectTagValue(ordType.getField())
 message.getField(symbol)
 message.getField(side)
 message.getField(orderQty)
 message.getField(price)
 message.getField(clOrdID)
 message.getField(quoteID)
 message.getField(currency)
```

The following code will create the *Execution Report* (35=8) message. The first line of this code creates an object execution report representing this message. The line after that will create the required headers for this message:

```
 executionReport = quickfix.Message()
 executionReport.getHeader().setField(beginString)
 executionReport.getHeader().setField(quickfix.MsgType(quickfix.MsgType_ExecutionReport))
 executionReport.setField(quickfix.OrderID(self.idGen.orderID()))
 executionReport.setField(quickfix.ExecID(self.idGen.execID()))
```

The following code takes care of building the code so that it simulates rejections. It will reject the code by taking a reject\_chance (a percentage) into account:

```
 try:
 reject_chance = random.choice(range(1, 101))
 if self.rejectRate > reject_chance:
 raise FixSimError("Rejected by cruel destiny %s" % str((reject_chance, self.rejectRate)))
```

The following code will run some checks on the execution size and the price:

```
 execPrice = price.getValue()
 execSize = orderQty.getValue()
 if execSize > quote.size:
 raise FixSimError("size to large for quote")
 if abs(execPrice - quote.price) > 0.0000001:
 raise FixSimError("Trade price not equal to quote")
```

The code will finish by populating the required fields of the *Execution Report* message:

```
 executionReport.setField(quickfix.SettlDate(self.getSettlementDate()))
 executionReport.setField(quickfix.Currency(subscription.currency))
 executionReport.setField(quickfix.OrdStatus(quickfix.OrdStatus_FILLED))
 executionReport.setField(symbol)
 executionReport.setField(side)
 executionReport.setField(clOrdID)
 executionReport.setField(quickfix.Price(price.getValue()))
 executionReport.setField(quickfix.AvgPx(execPrice))
 executionReport.setField(quickfix.LastPx(execPrice))
 executionReport.setField(quickfix.LastShares(execSize))
 executionReport.setField(quickfix.CumQty(execSize))
 executionReport.setField(quickfix.OrderQty(execSize))
 executionReport.setField(quickfix.ExecType(quickfix.ExecType_FILL))
 executionReport.setField(quickfix.LeavesQty(0))
```

The following code will build the rejection message in case of an error. It is done in the same way as building the message to indicate that the order has been executed. We specify the *Rejected* value in the *Order Status* of the *Execution Report* message:

```
except Exception as e:
 self.logger.exception("FixServer:Close order error")
 executionReport.setField(quickfix.SettlDate(''))
 executionReport.setField(currency)
 executionReport.setField(quickfix.OrdStatus(quickfix.OrdStatus_REJECTED))
 executionReport.setField(symbol)
 executionReport.setField(side)
 executionReport.setField(clOrdID)
 executionReport.setField(quickfix.Price(0))
 executionReport.setField(quickfix.AvgPx(0))
 executionReport.setField(quickfix.LastPx(0))
 executionReport.setField(quickfix.LastShares(0))
 executionReport.setField(quickfix.CumQty(0))
 executionReport.setField(quickfix.OrderQty(0))
 executionReport.setField(quickfix.ExecType(quickfix.ExecType_REJECTED))
 executionReport.setField(quickfix.LeavesQty(0))
```

Finally, we will send the message back to the initiator:

self.sendToTarget(executionReport, sessionID)

This concludes the part of the code that's specific to the acceptor. The role of the acceptor can be more rich than the bare minimum code we implement. The main role of the acceptor is to match orders between traders. If we were implementing an exchange, we would need to create a matching engine (to match orders that can be filled). In this simple example, we chose to fill our orders regardless of the state of the market. The main goal was just to build a simulation mimicking the behavior of the market by filling and rejecting orders.

## **Other trading APIs**

The FIX protocol has been used since 1992. By understanding FIX, which is a string-based protocol, you will be able to understand other protocols. Nasdaq uses the direct data feed, ITCH and the direct-trading OUCH protocol. These protocols are much faster than the FIX protocols because of their limit overhead. These protocols use a fixed offset to specify the tag values. For instance, instead of using 39=2, the OUCH protocol will use a value of 2 at an offset of 20.

The **New York Stock Exchange** (**NYSE**) uses UTP Direct, which is similar to the NASDAQ protocols. The cryptocurrency world uses HTTP requests while using the RESTful API or Websocket way of communicating. All of these protocols provide us with different ways to represent financial exchange information. They all have the same goal: price update and order handling.

## **Summary**

In this chapter, we learned that trading system communication is key to trading. The trading system is in charge of collecting the required prices to make an informed decision. If this component is slow, it will make the trading decision slower. Gateways are technically more challenging than any of the other components because they need to deal with the communication. The communication implies that layers are handled perfectly on the computer level; that is, the computer architecture (network layer), operating system (system calls, the driver that talks to the network card, and so on), and the software itself. All of these layers must be optimized so that they have a fast trading system. Because of their level of technical complexity, it is unlikely that you will implement this communication if you have strategies for high-frequency trading. Instead, you will use a system that's been provided by experts in this domain. However, if your trading strategy is not time-sensitive, you will be able to use the information you gained from this chapter to implement communication with the exchange.

We also talked about the communication between your trading system and exchanges. We learned how to use the Python *quickfix* library to simplify the time of the communication system's implementation. We used some software alongside quickfix to simulate exchanges between the initiator and the acceptor. By doing this, we learned about the workflows of trading communication systems. We are now aware of how to create a trading system and how to make this system communicate with the outside world. The last thing we need is to have confidence that the strategy will perform well on this trading system.

In the next chapter, we will talk about another critical step when it comes to testing a trading strategy: backtesting.

## **Creating a Backtester in Python**

By now, we know how to implement a trading strategy idea. We learned how to write the code to make it run in a trading system. The final step before going live with a trading strategy is backtesting. Whether you want to be more confident in the performance of your strategy or you want to show your managers how well your trading idea performs, you will have to use a backtester using a large amount of historical data.

In this chapter, you will learn how to create a backtester. You will improve your trading algorithm by running different scenarios with large amounts of data to validate the performance of your trading strategy. Once a model is implemented, it is necessary to test whether the trading robot behaves as expected in the trading infrastructure.

In this chapter, we will learn how backtesting works, and then we will talk about the assumptions you will need to consider when creating a backtester. Finally, we will provide a backtester example by using a momentum trading strategy.

In this chapter, we will cover the following topics:

- Learning how to build a backtester
- Learning how to choose the correct assumptions
- Evaluating what the value of time is
- Backtesting the dual-moving average trading strategy

## **Learning how to build a backtester**

Backtesting is key in the creation of trading strategies. It assesses how profitable a trading strategy is by using historical data. It helps to optimize it by running simulations that generate results showing risk and profitability before risking any capital loss. If the backtesting returns good results (high profits with reasonable risk), it will encourage getting this strategy to go alive. If the results are not satisfactory, backtesters can help to find issues.

Trading strategies define rules for entry and exit into a portfolio of assets. Backtesting helps us to decide whether it is worth going live with these trading rules. It provides us with an idea of how a strategy might have performed in the past. The ultimate goal is to filter out bad strategy rules before we allocate any real capital.

Backesting can sound out a run of a trading strategy using past market data. Most of the time, we consider a backtester like a model of reality. We will make assumptions based on the experience. But if the model is not close enough to reality, the trading strategies will end up not performing as well, which will result in financial losses.

The first part we will cover in this chapter is getting the data. The data will be stored in many different forms and, depending on them, we will need to adapt our backtester.

Backtesters use data heavily. In trading, getting 1 terabyte of data a day is pretty common. It can take a few minutes for a hard disk to read this amount of data. If you are looking for a specific range of dates, or if you are looking for specific symbols. It will be very important to have a performance index for the dates, the symbols, or other attributes. The data in finance is a value associated to a particular time, called time series. Regular relational databases are not efficient at reading these time series. We will review a few ways to handle time series.

# **In-sample versus out-of-sample data**

When building a statistical model, we use cross-validation to avoid overfitting. Cross-validation imposes a division of data into two or three different sets. One set will be used to create your model, while the other sets will be used to validate the model's accuracy. Because the model has not been created with the other datasets, we will have a better idea of its performance.

When testing a trading strategy with historical data, it is important to use a portion of data for testing. In a statistical model, we call training data the initial data to create the model. For a trading strategy, we will say that we are in the in-sample data. The testing data will be called out-of-sample data. As for cross-validation, it provides a way to test the performance of a trading strategy by resembling real-life trading as far as possible by testing on new data.

The following diagram represents how we divide the historical data into two different sets. We will build our trading strategy using the in-sample data. Then, we will use this model to validate our model with the out-of-sample data:

![](_page_78_Figure_0.jpeg)

When we build a trading strategy, it is important to set aside between 70% and 80% to build the model. When the trading model is built, the performance of this model will be tested out of the out-of-sample data (20- 30% of data).

## **Paper trading (forward testing)**

Paper trading (also known as forward performance testing) is the final step of the testing phase. We include the trading strategy to the real-time environment of our system and we send fake orders. After a day of trading, we will have the logs of all the orders and compare them to what they were supposed to be. This step is useful because it allows us to test the strategy and use the entire trading system.

This phase is a way to do a last test of the trading strategy before investing real money. The benefits of this phase are the absence of any financial risk whatsoever, while the trading strategy creator can acquire confidence and practice in a stress-free environment while building new datasets that will be used for further analysis. Unfortunately, performance obtained by paper trading is not directly correlated to the market. It is difficult to ensure that an order can be fulfilled, or not, and at what price. Indeed, during a period of high market volatility, most orders can be rejected. Additionally, orders could be fulfilled at a worse price (negative slippage).

## **Naive data storage**

One of the most intuitive ways to store data is to use flat file on the hard disk. The problem with this approach is that the hard disk will need to traverse a vast area to get to the part of a file corresponding to the data you would like to use for your backtesting. Having indexes can help enormously in looking up the correct segment to read.

## **HDF5 file**

The **Hierarchical Data Format** (**HDF**) is a file format designed to store and manage large amounts of data. It was designed in the 90s at the **National Center for Supercomputing Applications** (**NCSA**), and then NASA decided to use this format. Portability and efficiency for time series storage was key in the design of this language. The trading world rapidly adopted this format, in particular, **High-Frequency Trading** (**HFT**) firms, hedge funds, and investment banks. These financial firms rely on gigantic amounts of data for backtesting, trading, and any other kinds of analysis.

This format allows HDF users in finance to handle very large datasets, to obtain access to a whole section or a subsection of the tick data. Additionally, since it is a free format, the number of open source tools is significant.

The hierarchical structure of the HDF5 shown uses two major types:

- **Datasets**: Multidimensional arrays of a given type
- **Groups:** Container of other groups and/or datasets

The following diagram shows the hierarchical structure of the HDF5:

![](_page_81_Figure_7.jpeg)

To get the dataset's content, we can access it like a regular file using the POSIX syntax /path/file. The metadata is also stored in groups and datasets. The HDF5

format uses B-trees to index datasets, which makes it a good storage format for time series, especially financial asset price series.

In the code, we will describe an example of how to use an HDF5 file in Python. We will use the load\_financial\_data function we used in this book to get the GOOG prices. We store the data frame in an HDF5 file called goog\_data. Then, we use the h5py library to read this file and read the attributes of these files. We will print the data content of this files.

In this code will get the GOOG financial data. We store this data into the data frame goog\_data:

```
!/bin/python3
import pandas as pd
import numpy as np
from pandas_datareader import data
import matplotlib.pyplot as plt
import h5py
def load_financial_data(start_date, end_date,output_file):
 try:
 df = pd.read_pickle(output_file)
 print('File data found...reading GOOG data')
 except FileNotFoundError:
 print('File not found...downloading the GOOG data')
 df = data.DataReader('GOOG', 'yahoo', start_date, end_date)
 df.to_pickle(output_file)
 return df
 goog_data=load_financial_data(start_date='2001-01-01',
 end_date = '2018-01-01',
 output_file='goog_data.pkl')
```

In this part of the code we will store the data frame goog\_data into the file

goog\_data.h5.

```
 goog_data.to_hdf('goog_data.h5','goog_data',mode='w',format='table',data_columns=True)
```

We will then load this file from the file goog\_data.h5 and create a data

frame goog\_data\_from\_h5\_file:

```
goog_data_from_h5_file = h5py.File('goog_data.h5')
 print(goog_data_from_h5_file['goog_data']['table'])
 print(goog_data_from_h5_file['goog_data']['table'][:])
for attributes in goog_data_from_h5_file['goog_data']['table'].attrs.items():
 print(attributes)
```

Despite being portable and open source, the HDF5 file format has some important caveats:

- The likelihood of getting corrupted data is high. When the software handing the HDF5 file crashes, it is possible to lose all the data located in the same file.
- It has limited features. It is not possible to remove arrays.
- It offers low performance. There is no use of operating system caching.

Many financial companies still use this standardized file. It will remain on the market for a few years. Next, we will talk about the file storage alternative: databases.

## **Databases**

Databases are made to store data. Financial data is time series data, and most databases do not handle time series data in the most efficient way. The biggest challenge associated with storing time series data is scalability. An important data stream comes rapidly. We have two main groups of databases: relational and non-relational databases.

#### **Relational databases**

Relational databases have tables that can be written and accessed in many different ways without having the need to reorganize the database structure. They usually use **Structured Query Language** (**SQL**). The most widely used databases are Microsoft SQL Server, PostgreSQL, MySQL, and Oracle.

Python has many libraries capable of using any of these databases. We will use PostGresSQL as an example. The PostGresSQL library, Psycopg2, is used by Python to handle any SQL queries:

1. We will use the GOOG data prices to create the database for GOOG data:

```
goog_data.head(10)
 High Low Open Close Volume Adj Close
Date 2014-01-02 555.263550 550.549194 554.1259
2014-01-03 554.856201 548.894958 553.897461 548.929749 3355000.0 548.929749
2014-01-06 555.814941 549.645081 552.908875 555.049927 3561600.0 555.049927
2014-01-07 566.162659 556.957520 558.865112 565.750366 5138400.0 565.750366
2014-01-08 569.953003 562.983337 569.297241 566.927673 4514100.0 566.927673
2014-01-09 568.413025 559.143311 568.025513 561.468201 4196000.0 561.468201
2014-01-10 565.859619 557.499023 565.859619 561.438354 4314700.0 561.438354
2014-01-13 569.749329 554.975403 559.595398 557.861633 4869100.0 557.861633
2014-01-14 571.781128 560.400146 565.298279 570.986267 4997400.0 570.986267
2014-01-15 573.768188 568.199402 572.769714 570.598816 3925700.0 570.598816
```

2. To create a table in SQL, we will use the following command. You will need to install PostGresSQL on your machine. Then, you will need to insert the following content:

```
CREATE TABLE "GOOG"
 (
 dt timestamp without time zone NOT NULL,
 high numeric NOT NULL,
 low numeric NOT NULL,
 open numeric NOT NULL,
 close numeric NOT NULL,
 volume numeric NOT NULL,
 adj_close numeric NOT NULL
 CONSTRAINT "GOOG_pkey" PRIMARY KEY (dt)
 );
```

This command will create a SQL table named GOOG. The primary key of this table will be the timestamp, dt.

3. As an example, we will run the following query to get the GOOG data from 2016-11-08 to 2016-11-09:

```
SQL = '''SELECT 
 dt,high,low,open,close,volume, adj_close
 FROM "GOOG" 
 WHERE dt BETWEEN '2016-11-08' AND '2016-11-09' 
 ORDER BY dt 
 LIMIT 100;'''
```

The Python code will be the following:

```
import psycopg2
conn = psycopg2.connect(database='name_of_your_database') # set the appropriate credentials
cursor = conn.cursor()
def query_ticks():
 cursor.execute(SQL)
 data = cursor.fetchall()
 return data
```

The query\_ticks function will return the GOOG data.

The main issue with a relational database is speed. They are not made to work with large amounts of data indexed by time. To speed up, we will need to use non-relational databases.

#### **Non-relational databases**

Non-relational databases are very widespread. Because the nature of the data is increasingly based on time series, this type of database has developed rapidly during the last decade. The best nonrelational database for time series is called **KDB**. This database is designed to achieve performance with time series. There are many other competitors, including InfluxDB, MongoDB, Cassandra, TimescaleDB, OpenTSDB, and Graphite.

All of these databases have their pros and cons:

|             | Pros                              | Cons                                                            |
|-------------|-----------------------------------|-----------------------------------------------------------------|
| KDB         | High performance                  | Price; very difficult to use because of a non-SQL<br>language   |
| InfluxDB    | Free, performant, quick<br>start  | Small community; poor performance analysis tool,<br>no security |
| MongoDB     | Faster than rational<br>databases | No data joins; slow                                             |
| Cassandra   | Faster than rational<br>databases | Unpredictable performance                                       |
| TimescaleDB | SQL support                       | Performance                                                     |
| Graphite    | Free, widespread<br>support       | Performance                                                     |
| OpenTSDB    | Faster than rational<br>databases | Small number of features                                        |

As shown in the table, it is difficult to choose an alternative to KDB. We will code an example of Python code using the KDB library, pyq*.* We will create an example similar to the one we created for PostGresSQL:

```
from pyq import q
from datetime import date
# This is the part to be run on kdb
 #googdata:([]dt:();high:();low:();open:();close:();volume:(),adj_close:())
q.insert('googdata', (date(2014,01,2), 555.263550, 550.549194, 554.125916, 552.963501, 3666400.0, 552.963501))
 q.insert('googdata', (date(2014,01,3), 554.856201, 548.894958, 553.897461, 548.929749, 3355000.0, 548.929749))
 q.googdata.show()
 High Low Open Close Volume Adj Close
 Date
 2014-01-02 555.263550 550.549194 554.125916 552.963501 3666400.0 552.963501
 2014-01-03 554.856201 548.894958 553.897461 548.929749 3355000.0 548.929749
 # This is the part to be run on kdb
 # f:{[s]select from googdata where date=d}
x=q.f('2014-01-02')
 print(x.show())
 2014-01-02 555.263550 550.549194 554.125916 552.963501 3666400.0 552.963501
```

This code ends this section on data storage. This part is critical in the design of your backtester since the running time of your backtesting will enable you to save time so as to be able to run many more backtests to validate your trading strategy. Following this section on different ways of storing financial data, we will introduce how a backtester works.

## **Learning how to choose the correct assumptions**

Backtesting is a required step for deploying trading strategies. We use the historical data stored in databases to reproduce the behavior of the trading strategy. The fundamental assumption is that any methodology that functioned in the past is probably going to function in the future. Any strategies that performed ineffectively in the past are probably going to perform inadequately in the future. This section investigates what applications are utilized in backtesting, what sort of information is obtained, and how to utilize them.

A backtester can be a *for-loop* or *event-driven* backtester system. It is always important to consider how much time you will spend in order to achieve higher accuracy. It is impossible to obtain a model corresponding to reality; a backtester will just be a model of reality. However, there are rules to be followed in order to be as close as possible to the real market:

- **Training/testing data**: As with any models, you should not test your model with the data you use to create this model. You need to validate your data on unseen data to limit overfitting. When we use machine learning techniques, it is easy to overfit a model; that's why it is capital to use cross-validation to improve the accuracy of your model.
- **Survivorship-bias free data**: If your strategy is a long-term position strategy, it is important to use the survivorship-bias free data. This will prevent you from focusing on winners alone without considering the losers.
- **Look-ahead data**: When you build a strategy, you should not look ahead to make a trading decision. Sometimes, it is easy to make this mistake by using numbers calculated using the whole sample. This may be the case with an average that could potentially be calculated

within all the data; data that you shouldn't have since you calculate the average using just the prices you get before placing an order.

- **Market change regime**: Modeling stock distribution parameters are not constant in time because the market changes regime.
- **Transaction costs**: It is important to consider the transaction costs of your trading. This is very easy to forget and not to make money on the real market.
- **Data quality/source**: Since there are many financial data sources, data composition differs a lot. For instance, when you use OHLC data from Google Finance, it is an aggregation of many exchange feeds. It will be difficult to obtain the same highs and lows with your trading system. Indeed, in order to have a match between your model and reality, the data you use must be as close as possible to the one you will use.
- **Money constraint**: Always consider that the amount of money you trade is not infinite. Additionally, if you use a credit/margin account, you will be limited by the position you take.
- **Average daily volume (ADV)**: The average number of shares traded over a day for a given ticker. The quantity of shares you choose to trade will be based on this number so as to avoid any impact on the market.
- **Benchmark testing**: In order to test the performance of your trading strategy, you will compare against another type of strategy or just against the return of some indexes. If you trade futures, do not test against the S&P 500. If you trade in airlines, you should check whether the airline industry as a whole performs better than your model.
- **Initial condition assumption**: In order to have a robust way of making money, you should not depend on the day you start your backtesting or the month. More generally, you should not assume that the initial condition is always the same.
- **Psychology**: Even if we are building a trading robot, when we trade for real, there is always a way to override what the algorithm is doing, even if, statistically speaking, based on the backtest, a trading strategy can have a large dropdown but, after a few days, this strategy can bring in a lot of profit if we maintain a given position. For a computer, there are no problems with taking that risk but, for a human, it is more

difficult. Therefore, psychology can play a large role in the performance of a strategy.

On top of the prior rules, we will need to assume how we expect the market to behave. When you present a trading strategy to anyone, it is important to specify what these assumptions are.

One of the first assumption you need to consider is the fill ratio. When we place an order, depending on the type of strategies, the change of getting the order executed varies. If you trade with a high-frequency trading strategy, you may have 95% of the orders rejected. If you trade when there are important news on the market (such as FED announcements), you may have most of your orders rejected. Therefore, you will need to give a lot of thoughts on the fill ratio of your backtester.

Another important consideration is when you create a market making strategy. Unlike market trading strategies, a market making strategy does not remove liquidities from the market but add liquidities. Therefore it is important to create an assumption regarding when your order will be executed (or maybe it will not be executed). This assumption will add a condition to the backtester. We may get additional data. For instance, the trades which have been done in the market at a given time. This information will help us to decide whether a given market making order was supposed to be executed or not.

We can add additional latency assumptions. Indeed, since a trading system relies on many components. All the components have latencies and they also add latency when communicating. We can latency of any components of the trading systems, we can add network latency but also the latency to have an order executed, acknowledged.

The list of assumptions can be pretty long but it will be very important to show these assumptions to explain how likely your trading strategy will perform on the real market.

#### **For-loop backtest systems**

The for-loop backtester is a very simple infrastructure. It reads price updates line by line and calculates more metrics out of those prices (such as the moving average at the close). It then makes a decision on the trading direction. The profit and loss is calculated and displayed at the end of this backtester. The design is very simple and can quickly discern whether a trading idea is feasible.

An algorithm to picture how this kind of backtester works is shown here:

```
for each tick coming to the system (price update):
 create_metric_out_of_prices()
 buy_sell_or_hold_something()
 next_price()
```

## **Advantages**

The for-loop backtester is very simple to comprehend. It can be easily implemented in any programming language. The main functionality of this type of backtester is to read a file and calculate new metrics based on price alone. Complexity and the need for calculating power are very low. Therefore, execution does not take too long and it is quick to obtain results regarding the performance of the trading strategies.

## **Disadvantages**

The main weakness of the for-loop backtester is accuracy in relation to the market. It neglects transactions costs, transaction time, the bid and offer price, and volume. The likelihood of making a mistake by reading a value ahead of time is pretty high (look-ahead bias).

While the code of a for-loop backtester is easy to write, we should still use this type of backtester to eliminate low-performance strategies. If a strategy does not perform well with for-loop backtesters, this means that it will perform even worse on more realistic backtesters.

Since it is important to have a backtester that's as realistic as possible, we will learn how an event-driven backtester works in the following section.

### **Event-driven backtest systems**

An event-driven backtester uses almost all the components of the trading system. Most of the time, this type of backtester encompass all the trading system components (such as the order manager system, the position manager, and the risk manager). Since more components are involved, the backtester is more realistic.

The event-driven backtester is close to the trading system we implemented in Chapter 7, *Building a Trading System in Python*. We left the code of the TradingSimulation.py file empty. In this section, we will see how to code that missing code.

We will have a loop calling all the components one by one. The components will read the input one after the other and will then generate events if needed. All these events will be inserted into a queue (we'll use the Python deque object). The events we encountered when we coded the trading system were the following:

- Tick events When we read a new line of market data
- Book events When the top of the book is modified
- Signal events When it is possible to go long or short
- Order events When orders are sent to the market
- Market response events When the market response comes to the trading system

The pseudo code for an event-driven backtesting system is as follows:

```
from chapter7.LiquidityProvider import LiquidityProvider
from chapter7.TradingStrategy import TradingStrategy
from chapter7.MarketSimulator import MarketSimulator
from chapter7.OrderManager import OrderManager
from chapter7.OrderBook import OrderBook
from collections import deque
def main():
 lp_2_gateway = deque()
 ob_2_ts = deque()
```

```
 ts_2_om = deque()
 ms_2_om = deque()
 om_2_ts = deque()
 gw_2_om = deque()
 om_2_gw = deque()
 lp = LiquidityProvider(lp_2_gateway)
 ob = OrderBook(lp_2_gateway, ob_2_ts)
 ts = TradingStrategy(ob_2_ts, ts_2_om, om_2_ts)
 ms = MarketSimulator(om_2_gw, gw_2_om)
 om = OrderManager(ts_2_om, om_2_ts, om_2_gw, gw_2_om)
 lp.read_tick_data_from_data_source()
 while len(lp_2_gateway)>0:
 ob.handle_order_from_gateway()
 ts.handle_input_from_bb()
 om.handle_input_from_ts()
 ms.handle_order_from_gw()
 om.handle_input_from_market()
 ts.handle_response_from_om()
 lp.read_tick_data_from_data_source()
if __name__ == '__main__':
 main()
```

We can see that all the components of the trading system are called. If we had a service checking the position, this service would be called.

## **Advantages**

Because we use all the components, we will have a result that more closely corresponds to reality. One of the critical components is the market simulator (MarketSimulator.py). This component must have the same market assumptions. We can add the following parameters to the market simulator:

- Latency to send an acknowledgement
- Latency to send a fill
- An order filling condition
- A volatility filling condition
- A market making estimate

The advantages of the event-based backtester are as follows:

- Look-ahead bias elimination—since we receive events, we cannot look at the data ahead.
- Code encapsulation—because we use objects for the different parts of the trading system, we can just change the behavior of our trading system by changing the objects. The market simulation object is one such example.
- We can insert a position/risk management system and check whether we do not go against the limit.

## **Disadvantages**

Even if the advantages are numerous, we need to consider that this type of event-based system is difficult to code. Indeed, if there are threads in the trading system, we will need to make this thread deterministic. For instance, let's assume the trading system takes care of timing out if an order doesn't get a response within 5 seconds. The best practice to code this functionality would be to have a thread counting 5 seconds and then timing out. If we use the thread in backtesting, the time shouldn't be the real time because when we read the tick, the time will be the simulated time.

Additionally, it requires a lot of handling, such as log management, unit testing, and version control. The execution of this system can be very slow.

#### **Evaluating what the value of time is**

As we saw in the previous parts of this chapter, backtester accuracy is critical when we build a trading strategy. The two main components creating discrepancies between the paper trading of your trading strategy and the actual performance are as follows:

- The market behavior that we face when the trading strategy goes live
- The trading system that you use to trade

We saw that the market impact can be medicated by making assumptions regarding the manner in which the market will respond. This part is very challenging because it is just based on assumptions. As regards the second cause of discrepancies, the trading system itself, we can find an easy solution. We will be able to use the trading system as it is to be the backtester. We will get all the main trading components together and we will have them communicate between one another as if they were in production.

When we use the time in production, we can get the time from the computer's clock. For instance, we can stamp a book event coming to the trading strategy by just getting the time from the function *now* coming from the datetime module in Python. By way of another example, suppose we place an order. Because it is unsure whether the market will respond to this order, we will use a timeout system. This timeout system will call a function after a given period of time if no acknowledgement has been received by the trading system from the market. To accomplish this operation, we usually spawn a thread counting the number of seconds up to the timeout time. When counting, if the state of the order has not changed to acknowledge the order, this thread will call a callback function, onTimeOut. This callback will have the role of handling what should occur when an order timed out on the market. If we want to mock the timeout system in the backtester, this is going to be more challenging. Because we cannot use the realtime clock of the machine to count to the timeout time, we will need to use a simulated clock during the whole process.

The following diagram shows how the backtester will work with the new simulated clock component handling the time. Each time a component needs to get the time, it will call a function, getTime. This function will return the simulated time (being the time of the last tick read by the LiquidityProvider class):

![](_page_99_Figure_1.jpeg)

1. We will implement the **Simulated Clock** function (SimulatedRealClock class). Each time the trading system is started in backtest mode, we will use the SimulatedRealClock class with the simulated=True argument. If the trading system runs in real time to place orders on the market, the SimulatedRealClock class will be created without arguments or with the simulated=False argument, . When the time is given by a simulated time, the time will come from the order timestamps:

```
from datetime import datetime
class SimulatedRealClock:
 def __init__(self,simulated=False):
 self.simulated = simulated
 self.simulated_time = None
 def process_order(self,order):
 self.simulated_time= \
 datetime.strptime(order['timestamp'], '%Y-%m-%d %H:%M:%S.%f')
 def getTime(self):
 if not self.simulated:
 return datetime.now()
 else:
 return self.simulated_time
realtime=SimulatedRealClock()
print(realtime.getTime())
# It will return the date/time when you run this code
simulatedtime=SimulatedRealClock(simulated=True)
simulatedtime.process_order({'id' : 1, 'timestamp' : '2018-06-29 08:15:27.243860'})
```

```
print(simulatedtime.getTime())
# It will return 2018-06-29 08:15:27.243860
```

When coding a trading system, when you need the value of time, you will always need to use a reference to the SimulatedRealClock class and use the value returned by the getTime function.

2. In the following code, we will see the implementation of an order management system timing out 5 seconds after sending an order. We will first show you how to create a TimeOut class counting to the timeout value and calling a function when a timeout occurs. This TimeOut class is a thread. It means that the execution of this class will be concurrent to the main program. The arguments to build this class are the SimulateRealClock class, the time considered as the timeout time, and a function that will be called as a callback, fun. This class will run a loop as long as the current time is not older than the time to stop the countdown. If the time is higher and the TimeOut class has not been disabled, the callback function will be called. If the TimeOut class is disabled because the response to the order arrived in the system, the callback function will not be called. We can observe that we will compare the time to stop the timer with the current time by using the getTime function from the SimulatedRealClock class:

```
class TimeOut(threading.Thread):
 def __init__(self,sim_real_clock,time_to_stop,fun):
 super().__init__()
 self.time_to_stop=time_to_stop
 self.sim_real_clock=sim_real_clock
 self.callback=fun
 self.disabled=False
 def run(self):
 while not self.disabled and\
 self.sim_real_clock.getTime() < self.time_to_stop:
 sleep(1)
 if not self.disabled:
 self.callback()
```

3. The following OMS class that we will implement is just a small subset of what the order manager service can do. This OMS class will be in charge of sending an order. Each time an order is sent, a 5-second timeout will be created. This means that the onTimeOut function will be called if the OMS does not receive a response to the order placed on the market. We can observe that we build the TimeOut class by using the getTime function from the SimulatedRealClock class:

```
class OMS:
 def __init__(self,sim_real_clock):
 self.sim_real_clock = sim_real_clock
 self.five_sec_order_time_out_management=\
 TimeOut(sim_real_clock,
 sim_real_clock.getTime()+timedelta(0,5),
 self.onTimeOut)
```

```
 def send_order(self):
 self.five_sec_order_time_out_management.disabled = False
 self.five_sec_order_time_out_management.start()
 print('send order')
 def receive_market_reponse(self):
 self.five_sec_order_time_out_management.disabled = True
 def onTimeOut(self):
 print('Order Timeout Please Take Action')
```

When we run the following code to verify whether that works, we create two cases:

- **Case 1**: This will use the OMS in real time by using SimulatedRealClock in real-time mode.
- **Case 2**: This will use the OMS in simulated mode by using SimulatedRealClock in simulated mode.
- 4. In the following code, *Case 1* will trigger a timeout after 5 seconds, and *Case 2* will trigger a timeout when the simulated time is older than the time to trig the timeout:

```
if __name__ == '__main__':
 print('case 1: real time')
 simulated_real_clock=SimulatedRealClock()
 oms=OMS(simulated_real_clock)
 oms.send_order()
 for i in range(10):
 print('do something else: %d' % (i))
 sleep(1)
 print('case 2: simulated time')
 simulated_real_clock=SimulatedRealClock(simulated=True)
 simulated_real_clock.\
 process_order({'id' : 1,\
 'timestamp' : '2018-06-29 08:15:27.243860'})
 oms = OMS(simulated_real_clock)
 oms.send_order()
 simulated_real_clock. \
 process_order({'id': 1, \
 'timestamp': '2018-06-29 08:21:27.243860'})
```

When we use a backtester as a trading system, it is very important to use a class capable of handling simulation and real time. You will be able to achieve better accuracy by using the trading system and you will build better confidence in your trading strategy.

## **Backtesting the dual-moving average trading strategy**

The dual-moving average trading strategy places a buy order when the short moving average crosses the long moving average in an upward direction and will place a sell order when the cross happens on the other side. This section will present the backtesting implementation of the dual-moving average strategy. We will present the implementation of a for-loop backtester and an event-based backtester.

#### **For-loop backtester**

1. As regards the implementation of this backtester, we will use the GOOG data by retrieving it with the same function we used previously, load\_financial\_data. We will follow the pseudo code that we proposed during the previous section:

```
for each price update:
 create_metric_out_of_prices()
 buy_sell_or_hold_something()
 next_price();
```

We will create a ForLookBackTester class. This class will handle, line by line, all the prices of the data frame. We will need to have two lists capturing the prices to calculate the two moving averages. We will store the history of profit and loss, cash, and holdings to draw a chart to see how much money we will make.

The create\_metrics\_out\_of\_prices function calculates the long moving average (100 days) and the short moving average (50 days). When the short window moving average is higher than the long window moving average, we will generate a long signal. The buy\_sell\_or\_hold\_something function will place orders. The buy order will be placed when there is a short position or no position. The sell order will be placed when there is a long position or no position. This function will keep track of the position, the holdings, and the profit.

These two functions will be sufficient for this for-loop backtester.

2. Now, let's import the following libraries as shown in this code:

```
#!/bin/python3
 import pandas as pd
 import numpy as np
 from pandas_datareader import data
 import matplotlib.pyplot as plt
 import h5py
 from collections import deque
```

3. Next, as shown, we will call the load\_financial\_data function previously defined in this book:

```
 goog_data=load_financial_data(start_date='2001-01-01',
 end_date = '2018-01-01',
 output_file='goog_data.pkl')
# Python program to get average of a list
def average(lst):
 return sum(lst) / len(lst)
```

4. Let's now define the ForLoopBackTester class as shown. This class will have the data structure to support the strategy in the constructor. We will store the historic values for profit and loss, cash, positions, and holdings. We will also keep the realtime profit and loss, cash, position, and holding values:

```
class ForLoopBackTester:
 def __init__(self):
 self.small_window=deque()
 self.large_window=deque()
 self.list_position=[]
 self.list_cash=[]
 self.list_holdings = []
 self.list_total=[]
 self.long_signal=False
 self.position=0
 self.cash=10000
 self.total=0
 self.holdings=0
```

5. As shown in the code, we will write the create\_metric\_out\_of\_prices function to update the real-time metrics the trading strategy needs in order to make a decision:

```
 def create_metrics_out_of_prices(self,price_update):
 self.small_window.append(price_update['price'])
 self.large_window.append(price_update['price'])
 if len(self.small_window)>50:
 self.small_window.popleft()
 if len(self.large_window)>100:
 self.large_window.popleft()
 if len(self.small_window) == 50:
 if average(self.small_window) >\
 average(self.large_window):
 self.long_signal=True
 else:
 self.long_signal = False
 return True
 return False
```

6. The buy\_sell\_or\_hold\_something function will take care of placing the orders based on the calculation from the prior function:

```
 def buy_sell_or_hold_something(self,price_update):
 if self.long_signal and self.position<=0:
 print(str(price_update['date']) +
 " send buy order for 10 shares price=" + str(price_update['price']))
 self.position += 10
 self.cash -= 10 * price_update['price']
 elif self.position>0 and not self.long_signal:
 print(str(price_update['date'])+
 " send sell order for 10 shares price=" + str(price_update['price']))
 self.position -= 10
 self.cash -= -10 * price_update['price']
 self.holdings = self.position * price_update['price']
 self.total = (self.holdings + self.cash)
 print('%s total=%d, holding=%d, cash=%d' %
 (str(price_update['date']),self.total, self.holdings, self.cash))
 self.list_position.append(self.position)
 self.list_cash.append(self.cash)
 self.list_holdings.append(self.holdings)
 self.list_total.append(self.holdings+self.cash)
```

7. We will feed this class by using the goog\_data data frame as shown:

```
naive_backtester=ForLoopBackTester()
for line in zip(goog_data.index,goog_data['Adj Close']):
 date=line[0]
 price=line[1]
 price_information={'date' : date,
 'price' : float(price)}
 is_tradable = naive_backtester.create_metrics_out_of_prices(price_information)
 if is_tradable:
 naive_backtester.buy_sell_or_hold_something(price_information)
```

When we run the code, we will obtain the following curve. This curve shows that this strategy makes around a 50% return with the range of years we are using for the backtest. This result is obtained by assuming a perfect fill ratio. Additionally, we don't have any mechanism preventing drawdown, or large positions. This is the most optimistic approach when we study the performance of trading strategies:

![](_page_105_Figure_3.jpeg)

Achieving improved confidence in the way the strategy will perform in the market implies having a backtester that considers the characteristics of the trading system (more generally, the specificities of the company trading strategy where you work) and market assumptions. To make things more akin to scenarios encountered in real life, we will need to backtest the trading strategy by using most of the trading system components. Additionally, we will include the market assumptions in a market simulator.

In the following section, we will implement an event-based backtester handling the same GOOG data and we will be able to appreciate the differences.

#### **Event-based backtester**

The goal of the event-based backtester is to achieve better accuracy in the trading arena. We will consider the internals of the trading system by using the trading system we built in the last chapter and we will use the market simulator to simulate the external constraints of the market.

In this section, we will create an EventBasedBackTester class. This class will have a queue between all the components of the trading systems. Like when we wrote our first Python trading system, the role of these queues is to pass events between two components. For instance, the gateway will send the market data to the book through a queue. Each ticker (price update) will be considered an event. The event we implemented in the book will be triggered each time there is a change in the top of the order book. If there is a change in the top of the book, the book will pass a book event, indicating that there is a change in the book. This queue will be implemented using the deque from the collection library. All the trading object components will be linked to one another by these queues.

The input for our system will be the *Yahoo finance* data collected by the panda DataReader class. Because this data doesn't contain any orders, we will change the data with the process\_data\_from\_yahoo function. This function will use a price and will convert this price to an order.

The order will be queued in the lp\_2\_gateway queue. Because we need to fake the fact that this order will disappear after each iteration, we will also delete the order. The process\_events function will ensure that all the events generated by a tick have been processed by calling the call\_if\_not\_empty function. This function has two arguments:

- **A queue**: This queue is checked if empty. If this queue is not empty, it will call the second argument.
- **A function**: This is the reference to the function that will be called when the queue is not empty.

We will now describe the steps we will take to build the event-based backtester.

1. In the following code, we will import the objects we created during Chapter 7, *Building a Trading System in Python*. We will use the trading system we built as a backtester:

```
 from chapter7.LiquidityProvider import LiquidityProvider
 from chapter7.TradingStrategyDualMA import TradingStrategyDualMA
 from chapter7.MarketSimulator import MarketSimulator
 from chapter7.OrderManager import OrderManager
 from chapter7.OrderBook import OrderBook
 from collections import deque
 import pandas as pd
 import numpy as np
 from pandas_datareader import data
 import matplotlib.pyplot as plt
 import h5py
```

2. To read all the elements from a deque, we will implement the call\_if\_not\_empty function. This function will help to call a function as long as a deque is not empty:

```
def call_if_not_empty(deq, fun):
 while (len(deq) > 0):
 fun()
```

3. In the code, we will implement the EventBasedBackTester class. The constructor of this class will build all the deque needed to have all the components communicate. We will also instantiate all the objects in the constructor of

EventBasedBackTester:

```
class EventBasedBackTester:
 def __init__(self):
 self.lp_2_gateway = deque()
 self.ob_2_ts = deque()
 self.ts_2_om = deque()
 self.ms_2_om = deque()
 self.om_2_ts = deque()
 self.gw_2_om = deque()
 self.om_2_gw = deque()
 self.lp = LiquidityProvider(self.lp_2_gateway)
 self.ob = OrderBook(self.lp_2_gateway, self.ob_2_ts)
 self.ts = TradingStrategyDualMA(self.ob_2_ts, self.ts_2_om,\
 self.om_2_ts)
 self.ms = MarketSimulator(self.om_2_gw, self.gw_2_om)
 self.om = OrderManager(self.ts_2_om, self.om_2_ts,\
 self.om_2_gw, self.gw_2_om)
```

4. The process\_data\_from\_yahoo function will convert the data created by the panda DataReader class to orders that the trading system can use in real time. In this code, we will create a new order that we will then delete just after:

```
 def process_data_from_yahoo(self,price):
 order_bid = {
 'id': 1,
 'price': price,
 'quantity': 1000,
 'side': 'bid',
 'action': 'new'
 }
 order_ask = {
 'id': 1,
 'price': price,
 'quantity': 1000,
```

```
 'side': 'ask',
 'action': 'new'
 }
 self.lp_2_gateway.append(order_ask)
 self.lp_2_gateway.append(order_bid)
 self.process_events()
 order_ask['action']='delete'
 order_bid['action'] = 'delete'
 self.lp_2_gateway.append(order_ask)
 self.lp_2_gateway.append(order_bid)
```

5. The process\_events function will call all the components as long as we have new orders coming. Every component will be called as long as we didn't flush all the events in the deque:

```
 def process_events(self):
 while len(self.lp_2_gateway)>0:
 call_if_not_empty(self.lp_2_gateway,\
 self.ob.handle_order_from_gateway)
 call_if_not_empty(self.ob_2_ts, \
 self.ts.handle_input_from_bb)
 call_if_not_empty(self.ts_2_om, \
 self.om.handle_input_from_ts)
 call_if_not_empty(self.om_2_gw, \
 self.ms.handle_order_from_gw)
 call_if_not_empty(self.gw_2_om, \
 self.om.handle_input_from_market)
 call_if_not_empty(self.om_2_ts, \
 self.ts.handle_response_from_om)
```

6. The following code will instantiate the event-based backtester by creating the eb instance. Because we are going to load the same GOOG financial data, we will use the load\_financial\_data function. Then, we will create a for-loop backtester where will feed, one by one, the price updates to the event-based backtester:

```
 eb=EventBasedBackTester()
def load_financial_data(start_date, end_date,output_file):
 try:
 df = pd.read_pickle(output_file)
 print('File data found...reading GOOG data')
 except FileNotFoundError:
 print('File not found...downloading the GOOG data')
 df = data.DataReader('GOOG', 'yahoo', start_date, end_date)
 df.to_pickle(output_file)
 return df
 goog_data=load_financial_data(start_date='2001-01-01',
 end_date = '2018-01-01',
 output_file='goog_data.pkl')
for line in zip(goog_data.index,goog_data['Adj Close']):
 date=line[0]
 price=line[1]
 price_information={'date' : date,
 'price' : float(price)}
```

```
 eb.process_data_from_yahoo(price_information['price'])
 eb.process_events()
```

7. At the end of this code, we will display the curve representing the cash amount within the trading period:

```
 plt.plot(eb.ts.list_total,label="Paper Trading using Event-Based BackTester")
 plt.plot(eb.ts.list_paper_total,label="Trading using Event-Based BackTester")
 plt.legend()
 plt.show()
```

The new code that we introduce in this section is the code for the trading strategy. Our first trading strategy that we implemented in our trading system was an arbitrage strategy. This time, we will continue the example of the dual-moving average trading strategy.

This code shows that the logic of the trading strategy uses the same code as the for-loop backtester. The create\_metrics\_out\_of\_prices and buy\_sell\_or\_hold\_something functions are untouched. The main difference is regarding the *execution* part of the class. The execution takes care of the market response. We will be using a set of variables related to the paper trading mode to show the difference between actual and paper trading. Paper trading implies that every time the strategy sends an order, this order is filled at the price asked by the trading strategy. On the other side of the coin, the handle\_market\_response function will consider the response from the market to update the positions, holdings, and profit and loss.

8. We will code the TradingStrategyDualMA class inspired by the TradingStrategy class that we coded in Chapter 7, *Building a Trading System in Python*. This class will take care of keeping track of two series of values, the values for paper trading and the values for backtesting:

```
class TradingStrategyDualMA:
 def __init__(self, ob_2_ts, ts_2_om, om_2_ts):
 self.orders = []
 self.order_id = 0
 self.position = 0
 self.pnl = 0
 self.cash = 10000
 self.paper_position = 0
 self.paper_pnl = 0
 self.paper_cash = 10000
 self.current_bid = 0
 self.current_offer = 0
 self.ob_2_ts = ob_2_ts
 self.ts_2_om = ts_2_om
 self.om_2_ts = om_2_ts
 self.long_signal=False
 self.total=0
 self.holdings=0
```

```
 self.small_window=deque()
 self.large_window=deque()
 self.list_position=[]
 self.list_cash=[]
 self.list_holdings = []
 self.list_total=[]
 self.list_paper_position = []
 self.list_paper_cash = []
 self.list_paper_holdings = []
 self.list_paper_total = []
```

9. For each tick received, we will create a metric to make decisions. In this example, we use the dual-moving average trading strategy. Therefore, we will use two moving averages that we will build tick by tick. The create\_metric\_out\_of\_prices function calculates the short and long moving averages:

```
 def create_metrics_out_of_prices(self,price_update):
 self.small_window.append(price_update)
 self.large_window.append(price_update)
 if len(self.small_window)>50:
 self.small_window.popleft()
 if len(self.large_window)>100:
 self.large_window.popleft()
 if len(self.small_window) == 50:
 if average(self.small_window) >\
 average(self.large_window):
 self.long_signal=True
 else:
 self.long_signal = False
 return True
 return False
```

10. The buy\_sell\_or\_hold\_something function will check whether we have a long signal or a short signal. Based on the signal, we will place an order and we will keep track of the paper trading position, cash, and profit and loss. This function will also record the value of the backtested values of position, cash, and profit and loss. We will keep track of these values to create a chart of our trading execution.

```
def buy_sell_or_hold_something(self, book_event):
 if self.long_signal and self.paper_position<=0:
 self.create_order(book_event,book_event['bid_quantity'],'buy')
 self.paper_position += book_event['bid_quantity']
 self.paper_cash -= book_event['bid_quantity'] * book_event['bid_price']
 elif self.paper_position>0 and not self.long_signal:
 self.create_order(book_event,book_event['bid_quantity'],'sell')
 self.paper_position -= book_event['bid_quantity']
 self.paper_cash -= -book_event['bid_quantity'] * book_event['bid_price']
 self.paper_holdings = self.paper_position * book_event['bid_price']
 self.paper_total = (self.paper_holdings + self.paper_cash)
self.list_paper_position.append(self.paper_position)
 self.list_paper_cash.append(self.paper_cash)
 self.list_paper_holdings.append(self.paper_holdings)
 self.list_paper_total.append(self.paper_holdings+self.paper_cash)
 self.list_position.append(self.position)
```

```
 self.holdings=self.position*book_event['bid_price']
 self.list_holdings.append(self.holdings)
 self.list_cash.append(self.cash)
 self.list_total.append(self.holdings+self.cash)
```

11. As shown, the signal function will call the two prior functions:

```
def signal(self, book_event):
 if book_event['bid_quantity'] != -1 and \
 book_event['offer_quantity'] != -1:
 self.create_metrics_out_of_prices(book_event['bid_price'])
 self.buy_sell_or_hold_something(book_event)
```

12. The following function differs from the original function execution that we implemented in Chapter 7, *Building a Trading System in Python*. This one will keep track of the profit and loss, position, and the cash:

```
 def execution(self):
 orders_to_be_removed=[]
 for index, order in enumerate(self.orders):
 if order['action'] == 'to_be_sent':
 # Send order
            order['status'] = 'new'
            order['action'] = 'no_action'
            if self.ts_2_om is None:
 print('Simulation mode')
 else:
 self.ts_2_om.append(order.copy())
 if order['status'] == 'rejected' or 
 order['status']=='cancelled':
 orders_to_be_removed.append(index)
 if order['status'] == 'filled':
 orders_to_be_removed.append(index)
 pos = order['quantity'] if order['side'] == 'buy' else 
 -order['quantity']
 self.position+=pos
 self.holdings = self.position * order['price']
 self.pnl-=pos * order['price']
 self.cash -= pos * order['price']
 for order_index in sorted(orders_to_be_removed,reverse=True):
 del (self.orders[order_index])
```

13. As shown, the following function will handle the market response:

```
def handle_market_response(self, order_execution):
 print(order_execution)
 order,_=self.lookup_orders(order_execution['id'])
 if order is None:
 print('error not found')
 return
 order['status']=order_execution['status']
 self.execution()
```

14. The following function will return the profit and loss of the strategy:

```
def get_pnl(self):
 return self.pnl + self.position * (self.current_bid + self.current_offer)/2
```

When we run this example, we will obtain the following chart. We can observe that the curve is the same as the prior one. This means that the trading system that we created and the paper trading have the same reality:

![](_page_113_Figure_1.jpeg)

We will now modify the market assumptions by changing the fill ratio used by the market simulator. We are getting a fill ratio of 10%, and we can see that the profit and loss is profoundly impacted. Since most of our orders are not filled, we will not make money where the trading strategy was supposed to make money:

![](_page_114_Figure_0.jpeg)

The chart reminds us of the importance of having a fast system. If we place an order, in most cases, the order is rejected. This will negatively impact the profit and loss of the trading strategy.

# **Summary**

In this chapter, we highlighted how important backtesting is. We talked about two sorts of backtesters: a for-loop backtester, and an event-based backtester. We showed the two main differences and we implemented an example of both. This chapter concludes the creation path of a trading strategy. We initially introduced how to create a trading strategy idea, and then we explained how to implement a trading strategy. We followed that by explaining how to use a trading strategy in a trading system and then we finished our learning experience by showing how we can test a trading strategy.

In the next chapter, we will conclude this book by talking about your next steps in the algorithmic trading world.