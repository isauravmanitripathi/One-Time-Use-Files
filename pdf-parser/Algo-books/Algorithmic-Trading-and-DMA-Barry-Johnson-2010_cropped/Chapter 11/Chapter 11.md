![](_page_0_Picture_1.jpeg)

Algorithmic trading is just as reliant on its infrastructure as the financial theory upon which its rules are based.

# 11.1 Introduction

So far, in this book we have focussed on the theory behind trading strategies. However, implementing them also involves a considerable amount of infrastructure. Figure 11-1 shows a high-level overview of the main components that are required for algorithmic trading and DMA.

![](_page_0_Figure_5.jpeg)

Figure 11-1 A high level view of the infrastructure required for electronic trading

Clearly, order management is a key part of this process, without it nothing much would happen. Before we move on to look at some of the technical considerations for implementing trading algorithms let's first review the mechanics of order management.

## 11.2 Order management

Order management plays an important role in any trading. Just as orders are the basis of any strategy, so they must be entered and routed to the appropriate destination, as Figure 11-1 shows. Executions (or fills) and updates/confirmations must be propagated back so that we can track the status of any given order. This is all catered for by a wide range of platforms, available from brokers and third-party vendors. There are two main types, namely order management systems (OMSs) and execution management systems (EMSs). Table 11-1 summarises some of the key functions offered by these platforms.

| Function   |                                               | OMS          | EMS |
|------------|-----------------------------------------------|--------------|-----|
| Portfolio  | Modelling and rebalancing, "what-if" analysis |              |     |
| management | Portfolio accounting                          |              |     |
|            | Position management and P&L                   |              |     |
| Risk       | Risk management/exposure analysis             |              |     |
| management | Cash management                               |              |     |
|            | Commission tracking                           |              |     |
| Analytics  | Pre-trade analysis                            |              |     |
|            | Post-trade analysis                           |              |     |
|            | Real-time execution benchmarks                |              |     |
|            | Real time market data                         | $\checkmark$ |     |
| Execution  | Order book depth                              |              |     |
|            | Connectivity to brokers/routing networks/FIX  |              |     |
|            | DMA/Trading algorithms/crossing               | 0            |     |
|            | Trade confirmations/allocations               |              |     |
| Operations | Connectivity to back-office systems/STP       |              |     |
|            | Exception reporting /reconciliations          |              |     |

## Table 11-1 Typical OMS/EMS functions

Note that directories of the main OMS and EMS platforms may be found on the Advanced Trading website.<sup>1</sup>

Order management systems were originally developed to hclp improve workflow. They also encompass post-trade functionality, handling reporting and account allocation ready for clearing and settlement. They may also include portfolio-based functionality.

Execution management systems trace their roots back to the trade blotters and simple order entry screens that traders have relied on for decades. The adoption of DMA and algorithmic trading has led these to become increasingly sophisticated. Similarly, the increasing focus on transaction cost analysis has meant that many such systems now incorporate detailed pre-trade analytics.

At present, the level of convergence between OMSs and EMSs is growing rapidly. Fundamentally, though, whichever platform we use the mechanics of order entry and their subsequent routing are much the same. So let's examine each of these steps more closely.

<sup>&</sup>lt;sup>1</sup> Advanced Trading directories are available at www.advancedtrading.com/directories

## Order entry

Clearly, the main points to be captured for any order arc:

- the asset (a unique identifier or symbol)
- $\bullet$ the direction (whether we are buying or selling)
- the order size ٠
- ٠ any price limits (if applicable)
- any additional information detailing the order type and/or conditions ٠

As we saw in Chapter 4, there are a lot more types of order available than just market and limit orders. Similarly, a wide range of conditions may be applied to orders, allowing control over factors such as when and how long they are active, whether they may be partially filled and where they are routed. Therefore, order entry screens need to be able to support whatever order types and conditions are available for any given market.

Traders usually have a lot going on. Order entry needs to be a quick and painless operation. Symbol and account lookups must be fast to help ensure that order entry is as painless as possible. Order entry screens also need to make the appropriate options for order types and conditions easily available to the trader. For instance, Figure 11-2 shows an example order entry screen from the web version of the NASDAQ Workstation. Here we can easily select between different order types, routing destinations or change the time in force (TIF). We may create an iceberg order simply by setting a smaller display quantity. Likewise, there is a checkbox to activate pegging and an associated offset. So from a few drop down menus and check boxes a wide variety of order types is possible.

|               | Display                  |           | Price                 | Order Type       | Symbol             |
|---------------|--------------------------|-----------|-----------------------|------------------|--------------------|
|               | Attrib                   |           |                       | Limit            |                    |
|               |                          | Routing   |                       | Display Quantity | E 1x               |
|               | IntrMkt Sweep            | V<br>STGY |                       |                  | Sell               |
|               | Capacity                 |           | TIP                   | Total Quantity   | Short              |
|               |                          | 1OC       | 1/<br>$\nu \approx 2$ |                  | Exempt             |
|               | Received Date MM/DD/YYYY |           |                       | User Order ID    | Branch SQ#         |
| $\mathcal{A}$ |                          | 3/30/2007 |                       |                  |                    |
|               | Discretionary Offset     |           | Cap Price             | Offset           | Rev<br>Reg         |
|               | Clear                    | i: 000.00 | A: 000.00             | 8: 000.00        | Class              |
|               |                          |           |                       |                  | Pegged Orders<br>O |

Source: NASDAQ (2008) © Copyright 2008, The NASDAQ OMX Group, Inc. Reprinted with permission

Figure 11-2 An example order entry screen

Validation is also important, given all the possible permutations of orders and conditions across different venues/markets. Hence, order entry screens should ensure that selected options are all compatible and arc valid for the given market. Such validation is particularly important for DMA where the users may not be fully aware of all the intricacies of local market order types/conditions and regulations. It may also make sense to incorporate some "fat finger" logic, such as checking the overall order size or comparing it with the asset's average daily volume (ADV), to try to catch any mistakes.

With trading algorithms, the order entry screens tend to be more customised, since each algorithm has slightly different parameters and requirements. Often vendors also incorporate pre-trade analytics and/or transaction cost estimates to help with algorithm selection. For example, Figure 11-3 shows a sample screen taken from Morgan Stanley's Passport trading application. Since the screens are customised for each algorithm, all the necessary parameters are laid out in an intuitive fashion, allowing easy and accurate order entry.

![](_page_3_Figure_3.jpeg)

Source: © Morgan Stanley (2007)

Reproduced with permission from Morgan Stanley

#### Figure 11-3 An example algorithm entry screen

The rapid growth in the popularity of algorithmic trading, and the large number of algorithms involved, poses issues for OMS/EMS vendors. Keeping up with the rapid flow of new algorithms is difficult, particularly for those providing algorithms from a wide range of brokers. The screens for newer algorithms may well be queued up for testing and release by the various vendors. To gain access, clients will often need to upgrade their software. So, there can sometimes be a substantial delay before clients can get access to the latest algorithms.

One potential solution for this has been proposed by the Financial Information Exchange (FIX) group. Their algorithmic trading definition language (FIXatdl) is intended to ease the integration of algorithmic strategies by providing a consistent means of defining them. This XML-based<sup>2</sup> schema provides a standard framework for algorithm parameters, defining:

<sup>&</sup>lt;sup>2</sup> Extensible Markup Language (XML) is a general specification for annotating text, creating custom "languages".

- . Core data, such as their type and FIX tag
- Validation rules ٠
- User interface requirements

For example, the following XML snippet shows the configuration details for a "RiskLevel" parameter, based on an example from FIX (2007):

```
<pre></pre>
use="optional" minValue="1" maxValue="10" mutableOnCxlRpl="true"
controlType="Slider"/>
```

The core data represents the key information about each specific parameter, starting with its name. In this example, RiskLevel is mapped to the FIX tag number 7078. Its type is defined as an integer, although decimals, characters/strings and even enumerations are also supported. The use tag defines this as an optional parameter, whilst the  $\texttt{mutableOnCx1Rb1}$ tag refers to whether it may be modified in a subsequent update (in this case it can).

Validation rules may just be basic constraints, such as the minimum and maximum values shown in the RiskLevel example. Alternatively, they may be more complex, and based on combinations of parameters. The parameter type will also ensure a basic level of validation, such as between strings or numbers.

The user interface requirements determine how the parameter should appear in an order entry screen. In this case, the RiskLevel parameter will be shown as a slider, allowing the user to pick the most appropriate value between 1 and 10. Other supported widgets are check boxes, radio buttons, drop down list boxes (or combo boxes) and simple input fields for text or dates/times. A separate element, the strategyPanel, allows further control over how various parameters are grouped and displayed. For example, the following XML allows the screen shown in Figure 11-4 to be generated, by grouping together parameters within strategyPanels.

```
<stategyPanel orientation="horizontal">
    <strategyPanel title="Time Parameters" collapsible="false"
              orientation="vertical">
           <pre></pre>
              fixTag="168" use="optional" controlType="Clock"/>
           <pre></pre>
              fixTag="126" use="optional" controlType="Clock"/>
    </strategyPanel>
    <strategyPanel title="Advanced" collapsible="false"
              orientation="vertical">
           <pre></pre>
              fixTag="7022" use="optional" controlType="SingleSpinner"/>
           <pre></pre>
              fixTag="7023" use="optional" controlType="ComboBox">
                 <pre><enumPair uiRep="High" wireValue="3"/></pre>
                 <pre><enumPair uiRep="Medium" wireValue="2"/></pre>
                 <pre><enumPair uiRep="Low" wireValue="1"/></pre>
           </parameter>
    </strategyPanel>
</strategyPanel>
```

For more information on the FIXatdl specification, please see the overview provided by FIX (2008) or their website www.fixprotocol.org.

| Start Time     | Anarcas (000000000000000000000000000000000000<br>9:45:00 AM | Participation Rate | CONTRACT SANDARONANO AND AND AND AND<br>15            |  |
|----------------|-------------------------------------------------------------|--------------------|-------------------------------------------------------|--|
| <b>EndTime</b> | <br>11:45:00 AM                                             | Aggression         | and and an and an and an and an and an and an and and |  |

Source: © FIX (2008) www.fixprotocol.org

Reproduced with permission from FIX Protocol Ltd.

Figure 11-4 A simple FIXatdl algorithmic parameter screen

## Order routing

Once we have successfully entered our order we then need to route it to the required destination. In Figure 11-1 this is simply represented by some arrows going through a gateway process and then magically reaching the appropriate execution venue. In practice, each venue can have its own proprietary protocol for handling orders. Therefore, order routing systems have to convert (or encode) the details of each order into the appropriate format and then transmit them on to the required destination.

#### Order encoding

Before order routing was handled electronically, order encoding just meant using the right terms with your trader. Similarly, for trading pits, it meant knowing the correct hand signals to communicate the right price, side and size.

As venues have shifted to electronic trading, they have each implemented their own protocols for how orders should be processed. These are often accessed by custom application programming interfaces (APIs). Fortunately, a common messaging scheme, the Financial Information Exchange (FIX) Protocol, has become a de-facto standard for many markets. FIX is intended for the exchange of any information related to securities transactions. Hence, it supports the transmission of orders, market data, security information and settlement details. It exists in two main formats, a strictly machine-readable protocol and one based around an XML schema (FIXML).

The original FIX protocol is based on "Tag=Value" pairings, so an order to buy 1000 shares will contain the string " $54=1^38=1000$ ". For the first pair, 54 is the tag number that represents the side whilst the value 1 maps to a buy. Whereas tag 38 maps to the order size.

Each message begins with a standard format; this reflects the version of FIX, the length of the message and the message type (tag 35). It ends with a checksum that may be used for validation. Thus a message for a new order to buy 5000 shares of IBM looks like this, based on an example from FIX (2008a):

```
8=FIX.4.2<sup>9</sup>=251<sup>3</sup>5=D<sup>4</sup>9=AFUNDMGR<sup>5</sup>6=ABROKER<sup>3</sup>4=2<sup>5</sup>2=20030615-
01:14:49^11=12345^1=111111^63=0^64=20030621^21=3^110=1000^111=50000
^55=IBM^48=459200101^22=1^54=1^60=2003061501:14:49^38=5000^40=1^44=
15.75<sup>15</sup>=USD<sup>59</sup>=0<sup>10</sup>=127
```

(Note the  $\land$  character is just a representation of the separator between each pair.)

In this example, the message starts by stating the FIX version is 4.2, the message length is 251 bytes and the value of  $D$  refers to the fact that this message is for a new single order. Clearly, this approach is fine for sending messages between computer systems, but it is not very amenable for humans to read, for instance, during testing or debugging.

FIXML offers a more readable syntax, and since it is based on XML it allows developers to create custom filters or handlers. So for our example new order a FIXML representation looks something like this:

```
<FIXML><Order C1OrdID="12345"
              Side="1"
              TransactTm="2001-09-11T09:30:47-05:00"
              OrdTyp="2"
              Px="93.25"
              Acct="26522154">
              <Hdr
                     Snt="2001-09-11T09:30:47-05:00"
                      PosDup="N"
                      PosRsnd="N"
                      SeqNum="521">
                  <Sndr ID="AFUNDMGR"/>
                  <Tqt ID="ABROKER"/>
              \langle \text{Hdr} \rangle<Instrmt Sym="IBM" ID="459200101" IDSrc="1"/>
              <OrdQty Qty="5000"/>
      \langle /Order>
</FIXML>
```

Having replaced the numeric fields with more descriptive tags it is now easier to read the details. The groupings mean that the various parameters are placed with their associated tag, so we can clearly differentiate between the header details and those for the instrument. Though, some translation is still required. For example, the value of 1 for side means it is a buy order, whilst the value of 2 for OrdTyp means it is a limit order with a limit  $(Px)$  of 93.25. The instrument details confirm this is for IBM, both from the symbol and from the ID, which is based on a CUSIP. We can also see that the order is being sent from AFUNDMGR to ABROKER, using account 26522154. Finally, the message itself also has a unique client identifier (ClordID), namely 12345.

The main disadvantage with FIXML is the increased size of messages, which can cause capacity and performance issues for the required infrastructure. With earlier variants, the messages could be 3-5 times the size of an equivalent message using the FIX tag=value syntax. In version 4.4, the FIXML schema was updated to incorporate the latest XML enhancements. By streamlining the syntax and using more abbreviations the new FIXML messages are around 70% larger than the tag=value equivalents.

#### Handling different market types

FIX was originally created to handle the flow of orders. Though, it now also caters for quotedriven markets, supporting both the request for quote (RFQ) and request for stream (RFS) mechanisms that are commonly used in the fixed income and FX markets.

An RFQ based transaction starts with the client sending a Quote Request message to a specific broker. This may optionally specify both the Side and size (OrderQty), but the default is to request a standard market (two-way) quote. The broker must then respond with a corresponding Quote message in which they detail the price/s and size/s they are prepared to trade at. Alternatively, they may send a Quote Request Reject message. The client can then reply to the quote with a Quote Response, in which they can set the QuoteRespType field to "hit or lift" or to negotiate. Finally, if the RFQ results in a transaction the details are sent to the client in an Execution Report.

Streaming prices for RFS are handled via FIX's Market Data messages. Again these are triggered by a Market Data Request. An initial Market Data Snapshot is provided; quotes are then streamed through via subsequent Incremental Refresh messages. To trade in response to any given quote simply requires sending a new order based on the quoted price and size.

FIX also supports indications of interest (IOIs). To trade with any given Indication of Interest message means replying with an appropriate Quote Response, similar to the RFO mechanism.

#### Asset specific details

Initially, FIX initially catered solely for equities, but its range of supported asset classes has now expanded to include fixed income, foreign exchange, money market and derivatives. The current version of FIX  $(5.0)$  supports:

- Global equities  $\bullet$
- $\bullet$ US and European government and corporate bonds
- US agency and municipal securities  $\bullet$
- ٠ Repos
- US and European commercial paper  $\bullet$
- $\bullet$ FX spot, forwards and swaps
- Listed futures and options  $\bullet$

A wide variety of different instrument classification types are also catered for. Hence, fields are provided for data such as the maturity date or strike price. More complex, multi-leg assets, such as swaps, may be defined using the Security Definition message. These may then be transmitted between parties, each leg may be handled individually or as part of the whole. A similar approach may be used for futures, or options, spread trading strategies.

## **Order conditions**

Order conditions can offer significant additional functionality (and control of) their associated orders, as we saw in Chapter 4. The most important FIX tag for order conditions is TimeInForce; the permitted values are shown in Table 11-2.

| Value | Order type                |
|-------|---------------------------|
|       | Day (or session)          |
|       | Good Till Cancel (GTC)    |
| 2     | At the Opening (OPG)      |
| 3     | Immediate Or Cancel (tOC) |
| 4     | Fill Or Kill (FOK)        |
|       | Good Till Crossing (GTX)  |
| 6     | Good Till Date (GTD)      |
|       | At the Close              |
| 8     | Good Through Crossing     |
|       | At Crossing               |

#### Table 11-2 Permitted values for the FIX TimeInForce tag

The TimeInForce tag may be used to control order lifetimes with values such as Day or Good Till Cancel. For orders that are Good Till Date the deadline is specified with the ExpiryDate tag. Alternatively, it may also be used to determine whether the order permits partial fills; hence, there are values for immediate-or-cancel and fill-or-kill. It is also used to specify session requirements, such as at the opening or close.

#### Order types

FIX supports a wide range of order types, most of which are specified using its OrdType tag, as shown in Table 11-3:

| Value | Order type        |
|-------|-------------------|
|       | Market            |
|       | Limit             |
|       | Stop / Stop Loss  |
|       | Stop Limit        |
|       | Market If Touched |
|       | Pegged            |

## Table 11-3 Example values for the FIX OrdType tag

In addition, each of the order types uses its own custom tags to define additional parameters, such as a trigger price or offset value. Some examples are shown in Table 11-4.

| Order type     | Specific FIX tags                       |
|----------------|-----------------------------------------|
| Stop/StopLimit | StopPx                                  |
| Discretionary  | DiscretionInst<br>DiscretionOffsetValue |
| Pegged         | PegPriceType<br>PegOffsetValue          |
| Iceberg        | DisplayQty                              |

#### Table 11-4 Associated FIX tags for different order types

Stop and stop limit orders used to be specified in FIX by setting both the order type and the  $\text{StopPx}$  price field. In FIX 5.0, this approach has been replaced with a more sophisticated mechanism, based around the Triggering Instructions block. This allows for all sorts of triggered behaviours; changing the status, price and even size or type of orders. The TriggerAction dictates whether the trigger activates, modifies or cancels the affected order. The TriggerType determines what actually acts as the trigger, whether it is a price movement, a new trading session/auction or even partial execution. For pricedriven triggers, the TriggerPrice is similar to the old StopPx tag, whilst the TriggerPriceType determines which price is tracked, e.g. the last price or the best bid/offer. A TriggerPriceTypeScope field even supports the ability to base this on local market, national or global prices. The TriggerPriceDirection field specifics whether the trigger is hit on only rising or falling prices. Triggers may even be based on the prices of other assets, using the TriggerSymbol or TriggerSecurityID fields. This should permit triggers on futures or options to be based on the price of their underlying asset. In terms of what actually happens when the trigger is activated, the fields TriggerOrderType, TriggerNewPrice and TriggerNewOty allow control over the order's fundamental properties.

Discretionary orders are assigned by setting the DiscretionInst tag, relating this to the displayed price. The DiscretionOffsetValue defines the size of the price offset.

Pegged orders may be specified in FIX by setting the order type and the PegPriceType and PegOffsetValue tags. The PegPriceType supports pegging versus a wide range of prices, including the last trade, mid, open or even VWAP.

Iceberg, or reserve, orders are created by setting the  $DisplayQty$  tag. FIX also supports mixing and matching of these various types, so pegged orders may also incorporate discretionary pricing or iccherg behaviour etc., provided this is supported by the destination.

FIX can handle contingent order types as well, such as one-cancels-other. For this, the orders are created as a  $New$  Order - List and so are linked by their ListID tag. The ContingencyType tag then determines whether the relationship is one-cancels-other  $(1)$  or one-triggers-other (2).

#### Trading algorithms

FIX handles trading algorithms in a variety of ways. A nice introduction is provided by Roberto Rivero (2005) in FIXGlobal magazine. Clearly, we need to specify both the trading algorithm and its parameters.

There are several ways of setting the algorithm name in FIX messages. Exactly which method is used will depend on the broker/vendor's specific implementation. Table 11-5 shows some of the commoner types, as outlined in a presentation by Scott Atwell (2004) for the FIX Protocol Limited (FPL) Algorithmic Trading and DMA working group.

| Type             | FIX fields used                    |  |  |
|------------------|------------------------------------|--|--|
| Text             | TargetSubId(57) or Text(58)        |  |  |
| ExecInst/OrdType | ExecInst(18)or OrdType(40)         |  |  |
| TargetStrategy   | TargetStrategy (847)               |  |  |
| User Defined     | FIX custom tags in 5000–9999 range |  |  |

|  |  |  | Table 11-5 Different ways of specifying trading algorithms in FIX |  |  |
|--|--|--|-------------------------------------------------------------------|--|--|
|  |  |  |                                                                   |  |  |

Probably the commonest way is just to pass the algorithm's name ("VWAP", or "ImpShort", "POV") as a text field in one of the instruction tags, or in the user-defined custom fields (in the  $5000-9999$  range<sup>3</sup>).

For parameters, some existing FIX tags may be used. For instance, the start and end times may be defined by using the respective EffectiveTime and ExpireTime fields. Though, again it all depends on how the broker/vendor has chosen to implement things. Algorithm specific parameters will often be set using custom user-defined tags.

FIX 5.0 does provide a more generic means of handling algorithm parameters. There is a repeating group (NoStrategyParameters), which can contain any number of parameters. For each one a unique name is defined (StrategyParameterName) together with its type (StrategyParameterType) and value (StrategyParameterValue). For example, if an implementation shortfall algorithm needs to be passed a benchmark price and a risk aversion we could set these as follows:

```
NoStrategyParameters (957)
                           = 2StrategyParameterName(958)
                          = BenchmarkPrice
StrategyParameterType (959) = 8 (Price)StrategyParameterValue(960) = 7.4StrategyParameterName(958) = RiskAversionStrategyParameterType (959) = 1 (Int)StrategyParameterValue(960) = 5
```

<sup>&</sup>lt;sup>3</sup> These may be seen at http://www.fixprotocol.org/specifications/fields/5000-9999

As trading algorithms, OMS and EMSs evolve, the level of standardisation should hopefully improve, making it easier for the buy-side to switch between brokers without having to significantly change the format of their FIX messages.

#### Handling lists/portfolios

The FIX protocol also supports trading lists or portfolios. The  $New$  Order  $-$  List message allows a wave of orders to be sent, hased on a unique ListID. A ClordLinkID identifier may also be used to link orders. The constituent orders may still be updated or cancelled. However, FIX also provides an Order Mass Action Request that can be used to act on all the orders that match specific criteria. Similarly, there are equivalent requests to cancel orders en-mass or to query their status.

FIX even provides messages to handle the actual mechanics of portfolio trading. In the U.K. and U.S., this is often carried out via a blind auction, in which case the BidRequest message can be used to provide a summary model of the portfolio. This describes it in terms of its sectors, countries, indices and liquidity. The participating brokers may then reply with appropriate bids for the trade. The successful bidder will then be sent a  $New Order - List$ and the details of the actual portfolio. For some countries, such as Japan, the portfolio details may be disclosed for the auction; in which case the portfolio details are provided up-front, although the side may be left undefined. Principal trades are catered for as well, with a List Strike Price message, which may be used to detail the agreed strike prices for each constituent. Given that portfolio trades often span many different accounts, FIX messages may also be used to communicate any account allocation details, ready for settlement.

#### Order transmission

Having considered how to encode the orders, we now need to send them to their required destination. Order transmission brings us to the technical nitty-gritty of actually doing this. For the FIX protocol a lot of this logic is contained within specific FIX engine or gateway servers. These are readily available from a wide range of vendors. They understand the FIX message protocol and provide the necessary logic for establishing connections to other FIX engines/gateways.

Originally, these gateways were just used by clients to establish a direct connection to their brokers, as shown by pathway 1 in Figure 11-5. The broker would in turn have connections to the different execution venues, often these would be implemented using native APIs. Over time, though, an increasing number of execution venues have started to set up their own FIX gateways. Hence, clients now have the possibility of connecting directly to specific venues in addition to routing via their broker, as shown by the various pathways labelled 2 in Figure 11-5.

To ensure the data quality of messages they incorporate both check sums and message lengths, as we saw in the previous section. Thus, the FIX engine can confirm that the received message matches the one that was actually transmitted.

In terms of the actual transmission, clearly we want the connection to the broker/execution venue to be as resilient as possible. Consequently, when the FIX engine makes a connection it establishes a new session. All messages sent during this session are identified by a unique sequence number (MsqSeqNum). Messages should be delivered in order so if an engine receives a message whose identifier is out of sequence it can issue a resend request. Likewise, if an engine determines that there may have been a problem with transmitting the

![](_page_11_Figure_1.jpeg)

Figure 11-5 Potential transmission routes between clients, brokers and venues

message it may opt to retransmit it, setting the  $PosDupFlag$  to "Y". It is the responsibility of the receiving engine to then process the message, or discard it if it has already been successfully processed. During periods when no messages are being transmitted, heartbeat messages may also be sent, to confirm that the connection is still okay.

## 11.3 Algorithmic trading

Algorithmic trading is heavily dependent on both order management and market data services, as we saw back in Figure 11-1. A slightly more detailed infrastructure diagram for a typical algorithmic trading platform is shown in Figure 11-6.

Trading platforms are generally based on client-server technology, so an application on the trader's workstation interacts with a series of back-end servers. The price data for the OMS/EMS client is supplied by market data servers, whilst the actual orders are handled by dedicated order management servers. Algorithmic trading servers make use of both these services as well. They may also use dedicated analytics servers to process historical data or for back-testing. Some proprietary or risk-based algorithms may even use profit and loss  $(P&L)$  or risk servers to track their performance and/or exposure.

Most brokers' algorithmic trading platforms have been developed in-house over the last five to ten years. Often these have been built from the ground up. Millions of dollars and years of effort have been invested as each platform seeks to offer "best of breed" algorithms. This is combined with ensuring there is a resilient and scalable trading environment.

Third-party vendors also offer dedicated algorithmic trading platforms, often based on complex event processing (CEP) systems. These provide the basic constructs required for handling market data and processing orders and may even supply trading algorithms that can be extended or used as templates for brand new strategies. So implementing trading algorithms is now a much more viable proposition for the buy-side.

![](_page_12_Figure_1.jpeg)

Figure 11-6 A simple infrastructure for algorithmic trading

That said, building an algorithmic trading platform is not a decision to be taken lightly. It takes teams of developers, quants and experienced traders to create effective algorithms.

## Infrastructure requirements for algorithmic trading

As the usage of electronic and algorithmic trading continues to increase, the associated infrastructure will play just as key a role as the quality of the actual trading algorithms.

Building a successful platform for algorithmic trading is not just about having the best algorithms. If the infrastructure is not resilient, or sufficiently scalable then its use will be limited. Hence, it is important not to underestimate how much work is involved to create a successful trading platform.

## Speed/Latency

Speed has always been important in trading; however, the timescales involved have drastically reduced. People now talk in terms of microseconds  $(10^{-6}s)$ . To put this in perspective, a blink takes between 100-150 milliseconds  $(10^{-3}s)$ .

Latency is an often-used term. It represents the inherent delays in transmitting and processing data (for orders or market data prices). Figure 11-7 shows another version of the infrastructure diagram, highlighting the various stages that orders and prices go through.

So to get to the execution venue an order is sent from the client via the various gateways, arriving at the broker, as shown by path A. The algorithmic trading engine then sends out orders (again via gateways) to the execution venue, shown by paths B and C. Finally, the execution venue must receive and process the order (path D).

![](_page_13_Figure_1.jpeg)

Figure 11-7 Latency in infrastructure

Likewise prices from the execution venue are issued to market data vendors who then distribute them via their own infrastructure. Feed handlers at the broker (or client) receive these and then make them available to any processes that need them, again via their own infrastructure of market data servers. The overall trip times represent the total latency for sending an order or receiving a market data price, as shown by:

> $Total latency (order) = A + B + C + D$ Total latency (price) =  $1 + 2 + 3 + 4$

So there is no point having a super-fast connection to the external data sources, or execution venues, if internal processes are causing a significant delay. Conversely, there is no benefit in having a fast infrastructure with slow connections to external venues or market data.

Ideally, there should be the minimum number of steps so that data reaches its intended destination as fast as possible. Data messages should be as small as they can. Though, data can only be compressed so much. The time they take to be transmitted also depends on the physical distance they must travel. Table 11-6 shows the results of a round-trip test by Exponential-e (2009) for their routing service, to give an idea of the time it takes to communicate between different locations.

Thus, co-location has become increasingly popular. This allows market participants to host their computerised trading systems in the same machine rooms as the execution venue, thus minimising any transmission-related delays. Otherwise, U.S. based brokers will have considerable latencies when dealing with Asia or Europe, similarly European and Asian firms will be disadvantaged when handling orders for the U.S.

It is important to note that latencies will constantly vary, depending on the overall load. At times when the markets are busiest, or at their most volatile, the latencies will inevitably increase due to the higher workload. Therefore, is important to track latency at peak loads rather than focussing on a minimum figure, which will have been achieved given optimal conditions. In terms of infrastructure, things like careful load balancing can help ensure that processes do not become swamped by their workload, introducing additional delays.

| From:    | To:       | Latency/ms |
|----------|-----------|------------|
|          | Frankfurt | 10         |
| London   | New York  | 68         |
|          | Chicago   | 85         |
|          | Toronto   | 25         |
| New York | Zurich    | 90         |
|          | Tokyo     | 246        |
|          | Sydney    | 260        |

Source: Exponential-e (2009)

#### Table 11-6 A snapshot latency roundtrip comparison for some key locations

## Capacity

Over the last few years, electronic and algorithmic trading have led to smaller trade sizes and more frequent order updates. Consequently, the number of market data messages has massively increased, as we can see in Figure 11-8.

![](_page_14_Figure_6.jpeg)

Source: FIF (2009) Reproduced with permission from the Financial Information Forum

Figure 11-8 OPRA and consolidated equities 5 second peak rates

This shows the historical 5-second peak rates from the main market data feeds for U.S. equities and listed options. The increase is most notable for U.S. options. In fact messages from OPRA (Options Price Reporting Authority) now exceed 1.2 million messages per second, having nearly tripled in just two years.

In comparison, the equity feeds have lower update rates; indeed, all but the depth of book feeds (for NYSE AreaBook, NASDAQ TotalView ITCH and NASDAQ Level 2) are at the very bottom of Figure 11-8, with peak update rates below 200,000 messages per second.

These include the Consolidated Quotation System (CQS) and Consolidated Tape System (CTS) which carry the quote and trade updates for the NYSE (Tape A), Regional (Tape B) and the UTP Quotation Data Feed (UQDF) and UTP Trade Data Feed (UTDF) for NASDAQ (Tape C) stocks. They may be much lower, but the trend is the same, these have all seen considerable increases in update rates over the last few years.

Clearly, the numbers in Figure 11-8 are huge; however, they cover all the traded assets whose prices/trades are broadcast on each of the respective feeds. So the number of market data updates per second for a specific asset will obviously be a lot lower. No one algorithm will be exposed to hundreds of thousands of updates per second. Still, at any one time an algorithmic trading platform may be trading hundreds or thousands of different assets. Hence, these massive update rates become relevant, and the infrastructure will need to be able to cope with them.

#### **Other factors**

Speed and capacity are obviously important. However, reliability is also vital. A fast car is great, unless it breaks down every other day. So the infrastructure also needs to cope with every-day usage, as well as handling the loads at peak times. In modern markets, this may mean the infrastructure being available  $24x7$  (or as close as possible). Therefore, all of the server-side processes we saw back in Figure 11-6 also need to be:

- $\bullet$ Resilient
- Manageable .
- . Scalable

Hardware (or software) issues should not result in catastrophic failure. Therefore, if a machine or process fails there should be another machine/process ready to immediately take over in its place. This might be achieved by running machines/processes in fault-tolerant pairs, or using "server farms" to handle processes. Failures should also not be allowed to propagate, so a problem with analytics should not disable the algorithmic trading server.

Problems will always occur, so the infrastructure needs to be manageable. Failures should be simple to spot and correct. Monitoring should highlight the servers/processes that are under heavier load, since these may be more likely to fail in the future. Load balancing may also be adopted to try to ensure that the work is distributed evenly amongst the various processes/machines.

Scalability is another key issue. Obviously, for the long-term it is desirable to be able to easily extend capacity. There can also be short-term peaks in demand, so a flexible infrastructure where new servers can easily be added can be extremely useful.

## Designing an environment for algorithmic trading

Having considered some of the infrastructure surrounding electronic trading let's now take a closer look at how actual trading platforms might be designed and implemented. In Chapter 5, we saw a wide range of different trading algorithms. Still, they all share quite a lot of common functionality. Fundamentally, it all starts with an order, which details the trading requirements as well as the specifics for the algorithm. An instance of the algorithm will then be created with all these details. The trading algorithm's order placement decisions are fundamentally based on market data. Thus, it needs access to see the available prices and probably the liquidity. It also needs to be able to create, send and update orders to specific destinations, which will be one (or several) execution venues. Figure 11-9 shows a simple outline of these relationships.

![](_page_16_Figure_1.jpeg)

Figure 11-9 A simplified algorithmic trading environment

In terms of object-oriented programming (OOP), the above ellipses may be viewed as objects. Each of these is an instance of a specific class, which we will go through in the following sub-sections. They all "encapsulate" the required logic and data they need to work. In turn, they can be made up of other objects. For example, the order manager maintains a list of child orders which it is able to send on to the required destination.

Essentially, this also represents a minimal design for an algorithmic trading platform. In practice, it is slightly more complex than this, but by designing the environment based around suitable classes a lot of the complexity may be hidden.

#### Trading algorithm

The trading algorithm is effectively created from a parent order, which encapsulates the basic requirements such as the asset details, target size and direction (buy/sell) together with any price limit or specific conditions. The parent order also needs to maintain client details to ensure they can be provided with order status updates.

Based on the specified trading algorithm type and any associated parameters, the appropriate algorithm may then be launched. The trading algorithm contains all the various information needed for its execution. So it maintains market data subscriptions to get access to the prices etc. The algorithm also manages a list of all the child orders it has spawned, so if it is cancelled it can easily cycle through and cancel any extant orders. It also retains details such as the current position and maybe even its performance relative to any benchmarks. This information may then be used to determine whether it is ahead or behind of its targets, and so decide how aggressively future orders should be priced/sized. Obviously, there are also the actual trading rules; we will consider these in more detail in the next section.

#### Market data

Market data is generally provided for a specific asset at a set venue, although some vendors also provide consolidated feeds. Therefore, a subscription to the market data for an asset provides us with streaming updates for each time the price or size changes, or for when trade reports are issued.

Throughout this book, we have used order books to visualise the available liquidity, as shown in Figure 11-10. Because of the additional information value held within the order book, many exchanges and market data venues have variable charges for the different depths. Level 1 usually corresponds to the best bid and offer quotes, whilst Level 2 provides

|                      |             |         | Buys  |       |       | Sells |         |    |
|----------------------|-------------|---------|-------|-------|-------|-------|---------|----|
| Market data:         | Id          | Time    | Size  | Price | Price | Size  | Time    | Id |
| Level 1              | $\text{B}1$ | 8:24:00 | 1,000 | 100   | 101   | 1,000 | 8:25:00 | S  |
|                      | B2          | 8:21:25 | 5,000 | 99    | 102   | 1.500 | 8:20:25 | S2 |
| Level $2/3 \nmid B3$ |             | 8:23:25 | 2,500 | 98    | 104   | 2,000 | 8:19:09 | S3 |
|                      | B4          | 8:24:09 | 1,000 | 97    | 106   | 3,000 | 8:15:00 | S4 |

#### Figure 11-10 An example order book

a fuller view of the order book, although sometimes this aggregates orders. Sometimes there is even a Level 3, which gives a full view of the order book, except for hidden orders, of course. This data might be sourced from a single subscription, but often several different market data subscriptions will be required.

A dedicated order book class may be used to merge all this data together to provide a coherent image. Obviously, this translation needs to be fast so as not to introduce any significant additional latency. The order book class will also need to define its own custom events to correspond to any changes in the order book. In turn, classes for our trading rules may then subscribe to these events so as to be notified when the order book changes. This should allow our trading algorithms or execution tactics to react to any changes in liquidity.

Market data is also important for tracking reported trades. Algorithms such as POV need to track the market traded volume. Note that there can sometimes be substantial delays in trade reporting data; in fact, some might even be for previous days. So when reacting to trade ticks it is important to also check that the trade time and any conditions flags are appropriate.

Examining the reported trades is also important for tracking hidden liquidity, as we saw in Chapter 8. A custom order book class could be created which incorporates estimates for hidden liquidity. Though, again it is important to ensure that any calculations are performed as fast as possible, otherwise new data updates may render it meaningless.

#### **Orders**

Each child order that is spawned by the trading algorithm needs to contain its specific requirements. Namely, the asset details, target size and direction (buy/sell), together with any limit price or other conditions. It also needs some sort of identifier so that it may be linked back to the parent order/algorithm.

Orders lend themselves well to being implemented in a class. For instance, to send an IOC order with a limit price of 7.9 to a specific destination we could simply use code like:

```
Order myOrd = new LimitOrder( 7.9 );
<pre>myOrd.setCondition( ImmediateOrCancel );</pre>
myOrd.send( destination );
```

The send() method will handle the necessary encoding and transmission details. Hence, all the implementation details we saw in the previous sections remain hidden, keeping things a lot simpler.

One key consideration when handling orders is their state. Just because we have sent an order does not mean it has yet reached its intended destination. The transmission might fail or the destination may reject the order. So we should treat it as a pending order until we receive a successful acknowledgement. The same applies for any order updates or cancellations. This may mean certain actions are prevented, for example, a pending cancel might fail if the destination issues an update that the order has just been filled.

![](_page_18_Figure_1.jpeg)

Source: © FtX (2008b) www.fixprotocol.org Reproduced with permission from FtX Protocol Ltd.

Figure 11-11 FIX order states

A nice representation of the different states for a FIX order is provided in the documentation from FIX (2008b), as shown in Figure 11-11.

## Destination

Orders clearly need to be sent somewhere. Therefore, another key object that needs to be implemented is some sort of destination. This may simply be a wrapper for a connection to a FIX engine. The destination object might also incorporate additional logic, such as average latency information and details of any extra fees. This could then be used by any strategies that need to decide between execution venues.

## Other classes

Trading algorithms may also use a wide range of additional classes. For instance, VWAP algorithms need access to historical volume profiles. Cost-driven algorithms will need access to market impact and risk models. Liquidity-driven algorithms may use a diverse range of liquidity metrics. The logic associated with all of these analytics may be encapsulated in dedicated classes, which can then be shared between different trading algorithms.

## Implementing trading rules

So far, the trading algorithm class has just been a container. In order to recreate the algorithms we saw in Chapter 5 we need to add some actual trading logic to this. Typically,

![](_page_19_Figure_1.jpeg)

this means creating trading rules that respond to specific events or situations, as shown in Figure 11-12.

Figure 11-12 A rules-based trading algorithm

This event-based approach is common to most algorithmic trading platforms. Obviously, the key events are those related to market data, for prices and liquidity, and to orders, for fills and changes in status. Each rule will react to an event in a specific way, often by performing a set action. For example, a POV algorithm will need to take account of any new market volume; it might then update its target quantity or simply issue a new child order. Similarly, adaptive algorithms will react to changes in the market price or liquidity.

## Coding trading rules

Most algorithmic trading platforms are event-driven, built using an object-oriented language such as Java or  $C++$ ; so trading rules are often written directly in code.

In event-driven programming, each event represents a message that may be transmitted between objects. The objects are said to be either producers (publishers) or consumers (subscribers) for a specific event. So all the interested objects can register to ensure they are notified when an event occurs. These registrations may be handled by a separate intermediary, which allows the components to be "loosely coupled". Hence, the producers and consumers do not actually need to know any specifics about each other; all they require is access to the intermediary. This allows us to dynamically add new consumers or even change to use a different producer object. Such an approach provides a lot of flexibility.

The actual triggers are called event handlers. These respond every time a specific event happens. For instance, each time an order receives a fill an OrderFillEvent may be triggered. By registering a dedicated event handler for these we can be notified by this event each time the order gets a fill. We can then update our overall position based on the new fill size, as shown in the following sample event handler:

```
<pre>public void onOrderUpdate( OrderFillEvent oe ){</pre>
     if ( notYetProcessed( oe.getFillID() ) ) {
             <pre>position = position + oe.getFillSize();</pre>
             flagAsProcessed( oe.getFillID() );
```

}

}

```
adjustTarget();
```

In addition to updating the position we might also use this event to adjust our targets, as shown by the adjustTarget () placeholder. Note that the notYetProcessed() function simply protects us from situations when we might receive multiple confirmations for the same fill.

Market data provides two main types of information, firstly basic order book data such as the best bid and offer and their sizes. For example, let's consider recreating a simple pegging order. On each market data update (or tick) we check if the best bid or offer has changed:

```
<pre>public void onMarketDataUpdate( MarketDataEvent mde ){</pre>
     if ( mde.hasBestBidOrOfferChanged()
             && priceChangeSufficient() ){
                    doPeg();
     }
}
```

If the price change is sufficient, we need to change the price of our extant order, this decision is handled by the placeholder function priceChangeSufficient(). The doPeg() method contains all the necessary logic for the actual pegging. All the trading rule really does is act as a link to trigger this, based on the market data changing.

Market data events may also deliver information from trade reports. For example, a simple reactive Percent of Volume (POV) algorithm will need to respond to market data trade reports, setting its new target based on the additional volume:

```
<pre>public void onMarketDataUpdate( MarketDataEvent mde ){</pre>
     if ( mde.isTradeTick() && isValidTrade( mde ) ) {
             adjustTarget( mde.getTradeSize() );
             <pre>if ( targetChanged() )</pre>
                     sendOrder();
     }
```

}

The isValidTrade() function allows us to check the trade report flags and date to ensure this is volume the algorithm should be tracking. If the trade is valid a new target is then set. For a truly reactive POV approach, we can then issue an order, provided that the target size has changed sufficiently. Note that this is just a simple example, as we saw in Chapter 5 such a reactive approach is not the best way of implementing a POV algorithm.

Obviously, event handlers can be much more complex than these basic examples. For orders we also need to deal with rejections, cancellations etc., similarly for market data we need to handle order book information as well. We also need to deal with infrastructure issues, for instance, possible failures in the connections for our orders or our data feeds.

However, the key point is that complex behaviours can be built up from a large number of relatively simple rules. If they are designed well, the rules can often be used across a wide range of different strategies, and so helping to speed up development time for new strategies.

#### Scripting trading rules

Some vendor's platforms provide applications that allow trading rules to be scripted. A good example of this is the Apama Event Modeler as shown in Figure 11-13.

| Edit                                             | 🥯 statistical-arbitrage-sl - Event Modeler - [C. Program Files\Apama Event Modeler Professional Edition 2.1.0\scenarios\samples\statistical-arbitrage-sl sdf*]                                                                                                                                                                                                 |                                                                                                                                      | الال                                                                                                                                                                              |
|--------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| File<br>Tools<br>Window Help<br>Yiew.<br>4<br>W. | 7<br>CH.                                                                                                                                                                                                                                                                                                                                                       |                                                                                                                                      |                                                                                                                                                                                   |
| 我<br>Tates<br>State<br>100%<br>8                 | Local Rules - Check Quantities                                                                                                                                                                                                                                                                                                                                 | Scenario Variables<br>15 B<br>A.<br>4 2                                                                                              | 3<br>93<br>H.                                                                                                                                                                     |
| stan                                             | Volume Limit Check<br>Ensure that we do not breech any quantity limits (upper, i.e. buying; or lower, i.e. selling)<br>( $MaxQuantity$ is greater than or equal to ( Quantity: + ABS ( Current Position: ) ) ) and<br>When<br>{ MaxQuantity2 is greater than or equal to { Quantity2 + ABS { Current Position2 } } }<br>Then s move to state [Wait for spread] | value<br>name<br>brody us con<br>Q AW<br>Instrume<br><b>Orrandort</b><br>Chranelly?<br>kärsitmier.<br>MaxCum<br>MaxOttatt<br>Parment | outout<br>input<br>1111<br>N.<br>1<br>$\mathbb{Z}$<br>2<br>56.00<br>n<br>$\omega$<br>0<br>Ľ<br>V<br>6<br>K.<br>v<br>0.0<br>Ö<br>$\mathcal{L}$<br>0<br>Q.<br>0<br>C<br>V.<br>FALSE |
| Check Quantities<br>18<br>Wait for spread        | End<br>We will exceed our limits if we continue, so end the strategy. By moving to the end state, all<br>outstanding orders will be cancelled and the order flow ticks will be stopped.<br>When true (evaluated once)<br><sup>2</sup> StatusMosnage - "Limits Exceeded. Scenario Finished"<br>Then                                                             | Current<br>0 av<br>Current<br>Status#A<br>Trades L.<br>Spread<br>amead<br>Upper Ba<br>Lower S                                        | 1<br>0<br>Q.<br>0<br>S<br>mu<br>F.<br>a<br>V,<br>C.<br>V.<br>0.0<br>9<br>0.0<br>12                                                                                                |
| limits exceeded<br>no codorunity                 | move to state [end]                                                                                                                                                                                                                                                                                                                                            | Orai ases status<br>0102 Max. atstire<br>$\infty$<br>Blocks<br>12                                                                    | Q.<br>1<br>V,<br>12<br>4<br>K.<br>1                                                                                                                                               |
| Check spread<br>orders completed<br>isajoe       |                                                                                                                                                                                                                                                                                                                                                                | n'sme<br>💹 parsad<br>$\mathbb{R}$ nime                                                                                               | Spread Calculator (Spread Calculator vers<br>Stats (Data Distribution Calculator version<br>Vanie                                                                                 |
| Issue Orders                                     |                                                                                                                                                                                                                                                                                                                                                                | namo<br>instrument<br>service identifier<br>market identifier<br>🖁 extra parameter e                                                 | Market Depth 1 (Market Depth version 1.0)<br>ughe                                                                                                                                 |
| and                                              |                                                                                                                                                                                                                                                                                                                                                                | name<br>order identifier<br>service identifier<br>11.11                                                                              | Order Manager 2 (Order Manager version<br>48550<br>$\mathbf{v}$                                                                                                                   |

Source: Apama (2008) © 2008 Progress Software Corporation. Used with permission

#### Figure 11-13 A screenshot of the Apama Event Modeler

The Event Modeler provides a state-driven approach; the various potential states may be seen on the left hand side of Figure 11-13. The example scenario displayed is driven by the spread between the prices of two assets. The arrows show the progression from one state to another: So after starting and checking the quantities, the scenario effectively loops between the "wait for spread" and "check spread" states. Only when the spread is favourable will it shift to "issue orders". In the middle of Figure 11-13, we can also see the rules for the "check quantities" state. If it passes the 'volume limit check' rule then it will move to the "wait for spread" state. Otherwise, it will terminate with a status message noting that the limits have been exceeded.

This approach allows traders to create strategies by scripting appropriate rules within a custom application. Obviously, significant testing is still required, but it can offer a rapid means of prototyping new strategies.

## Testing

Testing is clearly a vital part of the process. The basic mechanism of each trading strategy and rule must be verified, so a dedicated test environment is usually required. This enables us to test each separate component for a wide range of market conditions. Back-testing may then be used to analyse the overall performance, based on historical data.

Note that whilst test environments are important there is no substitute for the real thing. Therefore, once they have passed all the various tests and performance analyses trading algorithms will often undergo a period of small-scale live testing. Only after careful realworld performance monitoring and analysis will the algorithms be ready for more widespread use.

#### Test environment

A test environment needs to be able to realistically recreate the actual infrastructure, so it will look similar to the layout we saw in Figure 11-1. Market data is important, similarly we need be able to dispatch orders and see their effect. Clearly, all these processes need to operate separately from the live production instances so that there is no confusion (or any accidents).

Testing against live market prices is certainly useful; however, historical (or "canned") data is often used as well. Live market prices are inherently uncertain, whereas using historical data allows us to control exactly what the market conditions are. This enables us to replay specific scenarios and so test the performance of a range of trading strategies, or rules, based on exactly the same conditions. A number of vendors already provide solutions which can store and replay historical data.

Validating the encoding and transmission of orders is also important, although admittedly these will change much less frequently than the trading rules. Often this will require a mix of visual inspection by the developers and routing orders through to test exchanges.

Another factor worth considering is latency. As strategies increasingly search for liquidity amongst different execution venues, they need to be able to take account of latency. Unfortunately, test environments often perform very differently to the real world, so simulators can play an important role in reproducing the effect of latency.

## Validating trading rules

As we have already seen, trading algorithms may be broken down into sets of trading rules. Each of these must be individually verified. So a developer may create specific tests to ensure that given the required market conditions each rule will react as expected. Thus, replaying historical market data is invaluable, since it allows fine-grained control of the market conditions. In comparison with live data, we simply cannot predict exactly how the market will move throughout the day, so there is no guarantee that a test condition will be triggered.

It is also important to test for extreme market conditions, such as during the 2007-09 linancial crisis. Consequently, testing may also be carried out using historical datasets for periods in which there was a strong price trend, volatility, trading halts or even sudden liquidity crises.

We also need to confirm how trading rules perform "en-masse" as part of an algorithm. For example, a perfectly reasonable stop-loss rule might actually play havoc with performance when incorporated into a liquidity-seeking algorithm. Careful post trade analysis can highlight the child orders that contributed most to the overall transaction costs. Then it is a matter of drilling down to understand why they were placed and to confirm whether this was the best approach.

#### **Back-testing**

Back-testing is an important method for verifying the potential performance and profitability of trading strategies. For instance, let's consider a trading strategy that relies on price forecasts based on historical moving average (MA) prices, as shown in Figure 11-14.

If the 10-day moving average rises above the 30-day moving average then we will treat this as a signal to buy the asset. Conversely, when it falls below the 30-day average we shall look to sell the asset. For this one example the rule seems to work quite well. Still, that does not guarantee its future success. A common way of validating its potential is to check how it does over time. By back-testing for the last few months we can determine whether the rule

![](_page_23_Figure_1.jpeg)

Figure 11-14 A simple trading strategy

holds true or whether it breaks down over time. Usually, this is gauged by determining the overall profit and loss (P&L) of a simulated strategy. Based on this figure we can then compare the performance of different trading strategies.

Note it is vital to remember that just because a rule holds for a certain period of historical data does not mean it will necessarily continue to do so in the future. As its name implies all back-testing does is highlight the performance based on data from the past. Factors such as transaction costs also play a key role: Just because a strategy seems profitable based on close prices does not mean it will actually be viable.

Trading algorithms can be back-tested, although the focus will usually be on performance rather than the overall P&L, since the decision to buy or sell remains a separate choice. Obviously, this requires a lot more data than simple close prices, simulations will need to incorporate data for each price "tick" and all the trades, as a bare minimum. They will also usually recreate the order book, so as to be able to replicate the exact market conditions.

Historical market data is invaluable for testing the fundamental behaviour of trading algorithms and rules. It is also important to remember that our trading strategies actually change market conditions. Each of our orders adds to the overall buying or selling pressure and so has an effect on both the market price and overall trading volume. Consequently, there is always some uncertainty about how the market will actually react to our orders.

Market impact and signalling risk are important factors, so for performance testing we need to try to simulate these effects. Though, as we saw in Chapter 10, accurately estimating market impact is non-trivial. Hence, simulators are often used to try to provide a realistic market for testing purposes. Any simulation must take into account competition from other participants and provide a realistic reaction to any test orders, whilst applying the same trade matching rules as the execution venue. Many of these will have been developed in-house, although increasingly vendors are offering exchange simulators that provide this.

The overall quality achieved using back-testing owes a lot to the accuracy of the market simulation. In Chapter 15, we will see how artificial intelligence is being used to try to make these simulations more accurate.

## 11.4 Other requirements

This chapter has mainly focussed on the technical requirements for implementing trading strategies. In order to successfully implement such strategies there are also some other important considerations: Generating thousands of electronic orders is all very well, but it could easily swamp the clearing and settlement department. Thus, it is vital to ensure that their infrastructure is able to cope with the potential load. In addition, trading platforms must adhere to the rules set out by the different execution venues that they use. So it is also important to audit them for regulatory compliance.

## Clearing and settlement

The ultimate goal of any trading platform is to execute trades quickly and efficiently. Although getting an execution back from an exchange is only half the story, since settlement still needs to take place.

Electronic trading has led to markedly increased trading volumes, which could have swamped the clearing and settlement departments. Fortunately, the shift away from manual trading has helped streamline the process, since most (if not all) of the trade-related information may now be processed electronically. This has increased the accuracy and allowed clearing and settlement to become more highly automated.

Just as the FIX Protocol has proved invaluable as a means of linking trading platforms, it also offers solutions for post-trade reporting and settlement. Once an order has been completed, an Execution Report message may be sent, detailing how much was filled and the average price. The client may then send an Allocation message to specify the actual accounts that should be used for settlement. Alternatively, they can even include this pre-trade in their New Order message. Finally, the broker may issue Confirmation messages that confirm each trade allocation, as well as the fees, account/s and other settlement details. More details can be found on the FIX website (www.fixprotocol.org).

As with any other piece of infrastructure, for a trading platform to be successful it is important that all its components are well integrated. Hence, the appeal of common protocols, such as FIX, which provide a uniform messaging structure allowing straightthrough processing (STP) from pre-trade right through to settlement.

## Regulations compliance

Trading must abide by market regulations, whether it is carried out manually or electronically. There is also scope to prevent potential problems by ensuring that systems perform basic "sanity checks" to ensure that orders are reasonable. These may be enforced by management or by dedicated compliance departments.

One of the advantages of electronic (and algorithmic) trading is that it is much easier to implement a full audit trail, tracking any order placements, changes and resultant executions, than it is for manual execution. This makes it easier to find the cause of any issues, should they occur.

## Sanity checks

Over the last few years, there have been several major instances of so-called "fat finger" trades. These are when someone accidentally enters an order with a ridiculous price or quantity, usually sending the asset's price spiralling downwards and resulting in the suspension of trading. It is important to ensure that there are systems and procedures in place to prevent such trades. This can be achieved by ensuring there are certain sanity checks to control orders':

- Price
- Size ٠
- Value

If any of these are significantly different from the norm then they probably warrant checking. These validations might be placed within the order entry screen, the order management system or both.

Clearly, the limit price is an important benchmark. If it bears no relation to the current market price this may be due to an input error. Alternatively, it might reflect a problem with currency conversion, or even issues with the market data source. For stocks, there might also have been a stock split or dividend, so it might be based on an old price.

Order sizes may be compared to the average daily volume (ADV). An order size that is more than 50% of the ADV might be a typo, or at least should be discussed carefully with the broker/dealer since it will need special handling.

By determining the overall value of the order we can add an extra level of validation. For example, both the price and size might be reasonable; however, if a client generally sends orders no larger than \$2 million then suddenly an order worth \$20 million arrives it may be an error.

Note that all of these checks are based on market data, so for them to be meaningful it is vital that the prices are valid and up to date. Thus, it is important for the order management system to have monitoring in place to ensure that market data is reliable and there is no significant latency in updates. Similarly, an algorithmic trading platform is blind without data, so such monitoring is even more important for these.

Trading algorithms also often make use of historical data and analytics, so it is important to ensure that there are mechanisms in place to check the validity of these as well. Again, a good example is coping with the historical adjustments required for stock splits.

#### Market regulations

Traders must pass exams in order to trade on most organised exchanges. This ensures that they have a thorough knowledge of the rules and regulations associated with trading and settlement. For instance, they will need to be aware of the:

- Trading sessions, both continuous and auction, and opening and closing times
- $\bullet$ Order types and conditions, and permitted combinations during each session
- $\bullet$ Trading halts/suspensions and market-wide halts
- Reporting requirements
- Code of conduct

Clearly, these regulations must be followed whether the trader is on the floor of the exchange, sending orders from a screen or using a trading algorithm. Therefore, order management systems must also be aware of these rules. Ideally, they should be able to prevent any incorrect orders from being sent to the execution venue. Order entry screens should also be aware of these and try to make life easier for the trader by only offering the appropriate options and/or combinations.

Algorithmic trading platforms must also incorporate the appropriate rules and regulations within their logic. For example, they should certainly be aware of the different trading sessions, such as continuous trading or a call auction, and adjust accordingly. They must also be aware of any market halts, or delays in opening or closing the market. Again, should this happen they need to be able to adjust their strategy accordingly, or as a minimum they ought to flag that there has been an issue and they require attention or manual intervention. Some venues even stipulate that electronic and algorithmic trading platforms have to be able to be turned off during periods of market instability. There should also be processes in place to handle any technical problems, such as failure of a market data server or the link to the exchange.

It is also important to review the logic behind trading algorithms, in order to try to prevent any accidental breaches of market regulations. As an example, let's consider an algorithm which is some way behind its targets. In trying to be filled, it might place an aggressive order. Though, if the market has already moved substantially throughout the day this might be enough to tip the balance and trigger a price-based halt. Ideally, there ought to be price checks in place to prevent this. Again, it is essential to test how algorithms respond to such events.

Clearly, a full system audit is a time consuming process; however, it is important to check that systems are compliant. In general, market regulations do not usually change that frequently. Thus, compliance checks are mainly needed when trading platforms and algorithms expand to cater for new markets. That said, this can all change when the markets become volatile. A good example of this is the rapid change of regulations for short-sales during the 2007-09 financial crisis. Indeed, given the resultant market turmoil regulation is likely to increase. For instance, there is the possible reintroduction of some form of uptick  $4$ rule for U.S. equities. Therefore, testing and auditing is a process that must continually evolve in order to keep pace with changes in the world's markets.

## 11.5 Summary

- Order management plays an important role in any trading strategy, it comprises of:
  - Order entry, allowing specification of any necessary trade conditions or parameters
  - Order encoding, to convert the details into a format the target venue can use
  - Transmission of order-related information to and from the venue
- Order management (OMS) and execution management (EMS) systems provide an important front-end for managing orders, as well as offering functions like pre- and post-trade analytics. They also connect to back-end servers, which handle the order encoding and routing.
- The Financial Information Exchange (FIX) protocol offers a common messaging  $\mathbf{r}$ scheme for the exchange of any information related to securities transactions. It handles the transmission of orders, market data, security information and settlement details. FIX (5.0) supports equities, bonds, repos, FX spot, forwards, swaps and listed futures and options.
- Algorithmic trading and DMA are reliant on their implementation, they need easily accessible platforms that are stable and can deal with heavy loads. They should also be easily extendable to increase capacity and allow new functionality.
- $\mathbf{L}$ Trading rules may be coded or scripted to respond to specific events, typically these are:
  - Market data, for prices and liquidity
  - Order notifications, for fills and changes in status
- Testing is a vital part of this process. Individual trading rules must be verified, but it is

<sup>&</sup>lt;sup>4</sup> Until its removal in 2007 this meant that short sales could only be carried out after the price had moved upwards.

also important to see how they perform en-masse, as part of an algorithm. Replaying specific scenarios allows the performance of a range of different rules to be compared based on exactly the same conditions. Though, it is also always important to test against live market data. Hence, brokers generally use algorithms internally for a while before making them available to their elients.

- Clearing and settlement must also be considered; it is important to ensure they can cope with the trading volume from electronic and algorithmic trading.
- $\blacksquare$ Trading platforms must also adhere to the rules set out by the different execution venues that they connect to, so it is essential to audit them for compliance.