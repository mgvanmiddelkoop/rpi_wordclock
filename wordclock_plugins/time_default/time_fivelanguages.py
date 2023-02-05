
class time_fivelanguages:
    """
    This class returns a given time as a range of LED-indices.
    Illuminating these LEDs represents the current time on a chinese WCA 10x10 (last 2 lines are fully dummy)

	It shows the time both in Chinese characters as in how to pronounce them,
	and additionally has a bonus sentence and some bonus words in Chinese characters:
	* Beautiful           - 佳         pronounced as Jiā
	* Love                - 爱         pronounced as Ài
	* Heart               - 心         pronounced as Xīn
	* Practice/experience - 练         pronounced as Liàn
    * Happy               - 高兴	       pronounced as Gāoxìng	
    	
	I have used this explanation https://improvemandarin.com/tell-time-in-chinese/
	In general: It is <hours> o'clock <minutes> / 1 or 3 quarters past / half past
	So no term for Minutes (not needed in non-formal chinese) and no X minutes before...
	On last thing: when using 5 minutes past, an extra "Ling" must be used for "zero-five".
		

   range(0,2) + range(12,13) + range(21,28) + range(63,67): 
    	It is ... o'clock: 现在 <xx> ... 点 and XIÀNZÀI <part of day> ... DIǍN 

	24 hour clock, since an indication of the part of the day is included.

	凌時		Líng shí	Midnight (left out of this clock, out of space)
	凌晨		língchén	12-5
	早上		zǎoshang	6-8
	上午		shàngwǔ		9-11
	中午		zhōngwǔ		12
	下午		xiàwǔ		1-5
	晚上		wǎnshàng	6-11
	
    十二		SHÍ ÈR		Twelve    
    一		YĪ			One       
    两		LIǍNG		Two       
    三		SÃN			Three     
    四		SÌ			Four       
    五		WǓ			Five       
    六		LIÙ			Six        
    七		QĪ			Seven      
    八		BÃ			Eight      
    九		JIÛ			Nine       
    十		SHÍ			Ten        
    十一		SHÍ YĪ		Eleven     
    十二		SHÍ ÈR		Twelve     

    零五		LÍNG WǓ		Five past           
    十		SHÍ			Ten past            
    十		SHÍ WǓ		Fifteen past    
    二十		ÈR SHÍ		Twenty past         
    二十五	ÈR SHÍ WǓ	Twenty five past    
    半		BÀN			Half past           
    三十五	SÃN SHÍ WǓ	Thirty five past    
    四		SÌ SHÍ		Fourty past         
    四五		SÌ SHÍ WǓ	Fourty five past 
    五十		WǓ SHÍ		Fifty past          
    五十五	WǓ SHÍ WǓ	Fifty five past     
            FEN

    self.full_hour= n/a
    """

    def __init__(self):
    
        self.maxlength = 0

        self.cnprefix = list(range(168,170)) +  list(range(199,200)) + list(range(220,227)) + list(range(322,326))
        self.cnhours= [\
            list(range(170,172))                        + list(range(227,231)) + list(range(240,244)) + list(range(178,179)) + list(range(180,181)) + list(range(288,291)) + list(range(315,317)), \
            list(range(170,172))                        + list(range(227,231)) + list(range(240,244)) + list(range(179,180))                        + list(range(291,293)), \
            list(range(170,172))                        + list(range(227,231)) + list(range(240,244)) + list(range(192,193))                        + list(range(295,300)), \
            list(range(170,172))                        + list(range(227,231)) + list(range(240,244)) + list(range(181,182))                        + list(range(317,320)), \
            list(range(170,172))                        + list(range(227,231)) + list(range(240,244)) + list(range(193,194))                        + list(range(300,302)), \
            list(range(170,172))                        + list(range(227,231)) + list(range(240,244)) + list(range(194,195))                        + list(range(277,279)), \
            list(range(172,173)) + list(range(174,175)) + list(range(244,247)) + list(range(250,255)) + list(range(195,196))                        + list(range(312,315)), \
            list(range(172,173)) + list(range(174,175)) + list(range(244,247)) + list(range(250,255)) + list(range(196,197))                        + list(range(320,322)), \
            list(range(172,173)) + list(range(174,175)) + list(range(244,247)) + list(range(250,255)) + list(range(197,198))                        + list(range(293,295)), \
            list(range(174,175)) + list(range(177,178)) + list(range(250,255)) + list(range(272,274)) + list(range(198,199))                        + list(range(274,277)), \
            list(range(174,175)) + list(range(177,178)) + list(range(250,255)) + list(range(272,274)) + list(range(199,200))                        + list(range(288,291)), \
            list(range(174,175)) + list(range(177,178)) + list(range(250,255)) + list(range(272,274)) + list(range(178,179)) + list(range(179,180)) + list(range(288,291)) + list(range(291,293)), \
            list(range(175,176)) + list(range(177,178)) + list(range(267,274))                        + list(range(178,179)) + list(range(180,181)) + list(range(288,291)) + list(range(315,317)), \
            list(range(176,177)) + list(range(177,178)) + list(range(264,267)) + list(range(272,274)) + list(range(179,180))                        + list(range(291,293)), \
            list(range(176,177)) + list(range(177,178)) + list(range(264,267)) + list(range(272,274)) + list(range(192,193))                        + list(range(295,300)), \
            list(range(176,177)) + list(range(177,178)) + list(range(264,267)) + list(range(272,274)) + list(range(181,182))                        + list(range(317,320)), \
            list(range(176,177)) + list(range(177,178)) + list(range(264,267)) + list(range(272,274)) + list(range(193,194))                        + list(range(300,302)), \
            list(range(176,177)) + list(range(177,178)) + list(range(264,267)) + list(range(272,274)) + list(range(194,195))                        + list(range(277,279)), \
            list(range(173,175))                        + list(range(247,255))                        + list(range(195,196))                        + list(range(312,315)), \
            list(range(173,175))                        + list(range(247,255))                        + list(range(196,197))                        + list(range(320,322)), \
            list(range(173,175))                        + list(range(247,255))                        + list(range(197,198))                        + list(range(293,295)), \
            list(range(173,175))                        + list(range(247,255))                        + list(range(198,199))                        + list(range(274,277)), \
            list(range(173,175))                        + list(range(247,255))                        + list(range(199,200))                        + list(range(288,291)), \
            list(range(173,175))                        + list(range(247,255))                        + list(range(178,179)) + list(range(179,180)) + list(range(288,291)) + list(range(291,293)), \
            list(range(170,172))                        + list(range(227,231)) + list(range(240,244)) + list(range(178,179)) + list(range(180,181)) + list(range(288,291)) + list(range(315,317))]

        self.cnminutes=[[], \
                                   list(range(216,217)) + list(range(217,218)) + list(range(218,219))                        + list(range(336,340)) + list(range(366,368)) + list(range(371,374)), \
                                   list(range(205,206))                        + list(range(218,219))                        + list(range(363,366))                        + list(range(371,374)), \
                                   list(range(205,206)) + list(range(217,218)) + list(range(218,219))                        + list(range(363,366)) + list(range(366,368)) + list(range(371,374)), \
            list(range(201,202)) + list(range(205,206))                        + list(range(218,219)) + list(range(343,345)) + list(range(363,366))                        + list(range(371,374)), \
            list(range(201,202)) + list(range(205,206)) + list(range(217,218)) + list(range(218,219)) + list(range(343,345)) + list(range(363,366)) + list(range(366,368)) + list(range(371,374)), \
            list(range(219,220))                                                                      + list(range(368,371)), \
            list(range(202,203)) + list(range(205,206)) + list(range(217,218)) + list(range(218,219)) + list(range(345,348)) + list(range(363,366)) + list(range(366,368)) + list(range(371,374)), \
            list(range(203,204)) + list(range(205,206))                        + list(range(218,219)) + list(range(348,350)) + list(range(363,366))                        + list(range(371,374)), \
            list(range(203,204)) + list(range(205,206)) + list(range(217,218)) + list(range(218,219)) + list(range(348,350)) + list(range(363,366)) + list(range(366,368)) + list(range(371,374)), \
            list(range(204,205)) + list(range(205,206))                        + list(range(218,219)) + list(range(360,362)) + list(range(363,366))                        + list(range(371,374)), \
            list(range(204,205)) + list(range(205,206)) + list(range(217,218)) + list(range(218,219)) + list(range(360,362)) + list(range(363,366)) + list(range(366,368)) + list(range(371,374))]
        self.cnfull_hour= []

        self.inprefix = list(range(285,288))
        self.inminutes= [[],\
            list(range(162,168)) + list(range(255,260)) + list(range(279,284)), \
            list(range(162,168)) + list(range(237,240)) + list(range(279,284)), \
            list(range(37,41)), \
            list(range(162,168)) + list(range(189,192)) + list(range(279,284)), \
            list(range(162,168)) + list(range(206,211)) + list(range(279,284)), \
            list(range(18,24)), \
            list(range(162,168)) + list(range(182,189)) + list(range(279,284)), \
            list(range(162,168)) + list(range(258,264)) + list(range(279,284)), \
            list(range(13,18)), \
            list(range(211,216)) + list(range(234,236)) + list(range(237,240)) + list(range(279,284)), \
            list(range(211,216)) + list(range(234,236)) + list(range(255,260)) + list(range(279,284)) ]
        self.inhours= [list(range(85,90)), \
            list(range(137,139)), \
            list(range(61,63)), \
            list(range(66,70)), \
            list(range(133,137)), \
            list(range(90,95)), \
            list(range(93,96)), \
            list(range(63,67)), \
            list(range(140,144)), \
            list(range(69,72)), \
            list(range(45,48)), \
            list(range(109,115)), \
            list(range(85,90))]
        self.infull_hour= list(range(157,161))

        self.nlprefix = list(range(0,3)) +  list(range(4,6))
        self.nlminutes=[[], \
            list(range(7,11)) + list(range(52,56)), \
            list(range(28,32)) + list(range(52,56)), \
            list(range(24,29)) + list(range(52,56)), \
            list(range(28,32)) + list(range(48,52)) + list(range(57,61)), \
            list(range(7,11)) + list(range(48,52)) + list(range(57,61)), \
            list(range(57,61)), \
            list(range(7,11)) + list(range(52,56)) + list(range(57,61)), \
            list(range(28,32)) + list(range(52,56)) + list(range(57,61)), \
            list(range(24,29)) + list(range(48,52)), \
            list(range(28,32)) + list(range(48,52)), \
            list(range(7,11)) + list(range(48,52)) ]
        self.nlhours= [list(range(72,78)), \
            list(range(129,132)), \
            list(range(127,131)), \
            list(range(78,82)), \
            list(range(144,148)), \
            list(range(148,152)), \
            list(range(105,108)), \
            list(range(96,101)), \
            list(range(120,124)), \
            list(range(100,105)), \
            list(range(123,127)), \
            list(range(81,84)), \
            list(range(72,78))]
        self.nlfull_hour= list(range(153,156))

        self.enprefix = list(range(384,386)) + list(range(387,389)) 
        self.enminutes=[[], \
            list(range(414,418)) + list(range(440,444)), \
            list(range(432,435)) + list(range(440,444)), \
            list(range(390,397)) + list(range(440,444)), \
            list(range(408,414)) + list(range(440,444)), \
            list(range(408,418)) + list(range(440,444)), \
            list(range(435,439)) + list(range(440,444)), \
            list(range(408,418)) + list(range(456,458)), \
            list(range(408,414)) + list(range(456,458)), \
            list(range(390,397)) + list(range(456,458)), \
            list(range(432,435)) + list(range(456,458)), \
            list(range(414,418)) + list(range(456,458)) ]
        self.enhours= [list(range(463,469)), \
            list(range(535,538)), \
            list(range(533,536)), \
            list(range(528,533)), \
            list(range(504,508)), \
            list(range(483,487)), \
            list(range(538,541)), \
            list(range(508,513)), \
            list(range(459,464)), \
            list(range(512,516)), \
            list(range(480,483)),\
            list(range(486,492)), \
            list(range(463,469))]
        self.enfull_hour= []

        self.spprefix = [] 
        self.spminutes=[[], \
            list(range(474,475)) + list(range(547,552)), \
            list(range(474,475)) + list(range(500,504)), \
            list(range(474,475)) + list(range(494,500)), \
            list(range(474,475)) + list(range(517,523)), \
            list(range(474,475)) + list(range(541,552)), \
            list(range(474,475)) + list(range(523,528)), \
            list(range(475,480)) + list(range(541,552)), \
            list(range(475,480)) + list(range(517,523)), \
            list(range(475,480)) + list(range(494,500)), \
            list(range(475,480)) + list(range(500,504)), \
            list(range(475,480)) + list(range(547,552)) ]
        self.sphours= [list(range(353,356)) + list(range(357,360)) + list(range(374,378)), \
            list(range(352,354)) + list(range(356,358)) + list(range(397,400)), \
            list(range(353,356)) + list(range(357,360)) + list(range(400,403)), \
            list(range(353,356)) + list(range(357,360)) + list(range(445,449)), \
            list(range(353,356)) + list(range(357,360)) + list(range(378,384)), \
            list(range(353,356)) + list(range(357,360)) + list(range(421,426)), \
            list(range(353,356)) + list(range(357,360)) + list(range(448,452)), \
            list(range(353,356)) + list(range(357,360)) + list(range(451,456)), \
            list(range(353,356)) + list(range(357,360)) + list(range(425,429)), \
            list(range(353,356)) + list(range(357,360)) + list(range(403,408)), \
            list(range(353,356)) + list(range(357,360)) + list(range(469,473)),\
            list(range(353,356)) + list(range(357,360)) + list(range(428,432)), \
            list(range(353,356)) + list(range(357,360)) + list(range(374,378))]
        self.spfull_hour= []

        self.temp = list(range(0,2)) +  list(range(12,13)) + list(range(25,29)) + list(range(30,33)) + list(range(60,64))
        self.wind= list(range(0,2)) +  list(range(12,13)) + list(range(25,29)) + list(range(30,33)) + list(range(60,64))
        self.cloud=list(range(0,2)) +  list(range(12,13)) + list(range(25,29)) + list(range(30,33)) + list(range(60,64))
        self.rain=list(range(0,2)) +  list(range(12,13)) + list(range(25,29)) + list(range(30,33)) + list(range(60,64))
        self.sun=list(range(0,2)) +  list(range(12,13)) + list(range(25,29)) + list(range(30,33)) + list(range(60,64))

    def get_time(self, time, purist):

        # Chinese
        hour=time.hour
        minute=time.minute//5
        #hour=time.hour%12 #+(1 if time.minute//5 > 3 else 0)
        
        # Assemble indices
        cnreturn = self.cnprefix + \
            self.cnminutes[int(minute)] + \
            self.cnhours[hour] + \
            self.cnfull_hour

            
        # Hindi
        hour=time.hour%12+(1 if time.minute//5 > 8 else 0)
        minute=time.minute//5
        
        if (minute == 6 and hour == 1):
        	inreturn = (self.inprefix if not purist else []) + \
        		list(range(116,120)) + \
        		self.infull_hour
        elif (minute == 6 and hour == 2):
        	inreturn = (self.inprefix if not purist else []) + \
        		list(range(41,45)) + \
        		self.infull_hour
        else:
            inreturn = \
                (self.inprefix if not purist else []) + \
                self.inminutes[int(minute)] + \
                self.inhours[hour] + \
                (self.infull_hour if (minute == 0) else [])


        # Dutch
        hour=time.hour%12+(1 if time.minute//5 > 3 else 0)
        minute=time.minute//5

        nlreturn = \
            (self.nlprefix if not purist else []) + \
            self.nlminutes[int(minute)] + \
            self.nlhours[hour] + \
            (self.nlfull_hour if (minute == 0) else [])


        # English
        hour=time.hour % 12+(1 if time.minute//5 >= 7 else 0)
        minute=time.minute//5
        # Assemble indices
        enreturn = \
            (self.enprefix if not purist else []) + \
            self.enminutes[int(minute)] + \
            self.enhours[hour] + \
            (self.enfull_hour if (minute == 0) else [])

        
        
        # Spanish
        hour=time.hour % 12+(1 if time.minute//5 >= 7 else 0)
        minute=time.minute//5
        # Assemble indices
        spreturn = \
            (self.spprefix if not purist else []) + \
            self.spminutes[int(minute)] + \
            self.sphours[hour] + \
            (self.spfull_hour if (minute == 0) else [])            
        
        fivelanguagesreturn = inreturn + cnreturn + nlreturn + enreturn + spreturn
        
        #calculate maximum nr of lighted leds
        if (len(fivelanguagesreturn) > self.maxlength):
            self.maxlength = len(fivelanguagesreturn)
            print(self.maxlength)

        return fivelanguagesreturn

