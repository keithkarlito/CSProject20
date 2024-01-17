import random
import os
def clear():
	os.system('clear')

#CLASS DECLARATION
class LeaderboardListNode:
	def __init__(self):
		self.Data = ""
		self.Pointer= -1

#CLASS DECLARATION
class User:
	def __init__(self,n):
		self.__Score=1000
		self.__RoundNo=1
		self.__PreviousTopic=-1
		self.__Name=n	
		self.__TopicList=["Cars","General Knowledge","Sport","Geography","Science","Technology"]
		self.__LineNoOfQuestionsRepeated=[0 for i in range(0,7)]

	
	def NoQuestionsRepeated(self,LineNo):
		Valid=True
		i=0
		while i!=(self.__RoundNo)-1 and Valid==True:
			if LineNo==self.__LineNoOfQuestionsRepeated[i]:
				Valid=False
			i=i+1
		if Valid==True:
			self.__LineNoOfQuestionsRepeated[i]=LineNo
		return (Valid)
	
	def SetScore(self,AnswerChoice,AnswerIndex):
		A,B,C,D=AnswerChoice.split(",")
		if AnswerIndex==0:
			self.__Score=int(A)
		elif AnswerIndex==1:
			self.__Score=int(B)
		elif AnswerIndex==2:
			self.__Score=int(C)
		elif AnswerIndex==3:
			self.__Score=int(D)

	def SetPreviousTopic(self,TopicNo):
		self.__PreviousTopic=TopicNo
	
	def IncrementRoundNo(self):
		self.__RoundNo=self.__RoundNo+1
	
	def GetName(self):
		return(self.__Name)
	
	def GetScore(self):
		return(self.__Score)
	
	def GetPreviousTopic(self):
		return(self.__PreviousTopic)

	def GetTopic(self,Index):
		return(self.__TopicList[Index])
	
	def GetRoundNo(self):
		return(self.__RoundNo)

#CLASS DECLARATION
class QuestionAndOptions:
	def __init__(self):
		self.__Question=""
		self.__Answer=""
		self.__Option1=""
		self.__Option2=""
		self.__Option3=""
			
	def SetQuestionAndAnswers(self,ThisLine):
		EncryptedQuestion, EncryptedAnswer, EncryptedOption1, EncryptedOption2, EncryptedOption3,EmptySpace=ThisLine.split("_")
		for i in range(0,len(EncryptedQuestion)):
			self.__Question=self.__Question+chr(ord(EncryptedQuestion[i])-3)
		for i in range(0,len(EncryptedAnswer)):
			self.__Answer=self.__Answer+chr(ord(EncryptedAnswer[i])-3)	
		for i in range(0,len(EncryptedOption1)):
			self.__Option1=self.__Option1+chr(ord(EncryptedOption1[i])-3)
		for i in range(0,len(EncryptedOption2)):
			self.__Option2=self.__Option2+chr(ord(EncryptedOption2[i])-3)
		for i in range(0,len(EncryptedOption3)):
			self.__Option3=self.__Option3+chr(ord(EncryptedOption3[i])-3)
	
	def OutputRandomOrder(self):
		OutputOptionList= ["" for i in range(0,4)]
		AnswerIndex=random.randint(0,3)
		OutputOptionList[AnswerIndex]=self.__Answer
		#Option1
		i= random.randint(0,3)
		while OutputOptionList[i]!="":
			i=random.randint(0,3)
		OutputOptionList[i]=self.__Option1
		#Option2
		i= random.randint(0,3)
		while OutputOptionList[i]!="":
			i=random.randint(0,3)
		OutputOptionList[i]=self.__Option2
		#Option3
		i= random.randint(0,3)
		while OutputOptionList[i]!="":
			i=random.randint(0,3)
		OutputOptionList[i]=self.__Option3
		print("\n|QUESTION: ", self.__Question,"|")
		print("A.",OutputOptionList[0]," B.",OutputOptionList[1], " C.",OutputOptionList[2]," D.",OutputOptionList[3])
		return (AnswerIndex)

	def GetAnswer(self):
		return(self.__Answer)

def InitialiseList():
	LeaderboardList= [LeaderboardListNode() for i in range(0,100)]
	for i in range (0,99):
		LeaderboardList[i].Pointer= i+1
	LeaderboardList[99].Pointer= -1
	StartPointer=-1
	FreeListPointer=0
	return(LeaderboardList, StartPointer,FreeListPointer)

def InsertNode(LeaderboardList, StartPointer,FreeListPointer,LeaderboardLine):
	if FreeListPointer != -1:
		NewNodePointer=FreeListPointer
		LeaderboardList[NewNodePointer].Data= LeaderboardLine
		FreeListPointer= LeaderboardList[FreeListPointer].Pointer
		PreviousNodePointer=-1
		ThisNodePointer= StartPointer
		while ThisNodePointer!= -1 and LeaderboardList[ThisNodePointer].Data> LeaderboardLine:
			PreviousNodePointer=ThisNodePointer
			ThisNodePointer= LeaderboardList[ThisNodePointer].Pointer
		if PreviousNodePointer==-1:
			LeaderboardList[NewNodePointer].Pointer= StartPointer
			StartPointer=NewNodePointer
		else:
			LeaderboardList[NewNodePointer].Pointer= LeaderboardList[PreviousNodePointer].Pointer
			LeaderboardList[PreviousNodePointer].Pointer= NewNodePointer
	else:
		print (" LEADERBOARD FULL")
	return (LeaderboardList, StartPointer, FreeListPointer)

def PrintLeaderBoardList (LeaderboardList, StartPointer):
	CurrentNodePointer= StartPointer
	print("------------------------------------------LEADERBOARD:------------------------------------------")
	if CurrentNodePointer!=-1:
		LeaderboardPosition=1
		while CurrentNodePointer!= -1:
			Score,Name,EmptySpace=(LeaderboardList[CurrentNodePointer].Data).split("_")
			print (LeaderboardPosition,". ",Score,"-> ",Name)
			CurrentNodePointer= LeaderboardList[CurrentNodePointer].Pointer
			LeaderboardPosition=LeaderboardPosition+1
	else: print('LEADERBOARD IS EMPTY')	
	print("------------------------------------------------------------------------------------------------")


def CreateInitialLeaderboard():
	LeaderboardList, StartPointer, FreeListPointer= InitialiseList()
	Leaderboard=open("LeaderboardFile.txt","r")
	LeaderboardLine=Leaderboard.readline()
	while len(LeaderboardLine)>0:
		LeaderboardList, StartPointer, FreeListPointer= InsertNode(LeaderboardList, StartPointer, FreeListPointer, LeaderboardLine)
		LeaderboardLine=Leaderboard.readline()
	Leaderboard.close	
	return LeaderboardList,StartPointer,FreeListPointer
def Choice():
	print("------------------------------------------------------------------------------------------------")
	print("Press N for a new game")
	print("Press X to end game")
	print("Press L for to view the current leader board","\n")
	Selection=input("Enter Choice:")
	while Selection!="X" and Selection!="x" and Selection!="N" and Selection!="n" and Selection!="L" and Selection!="l":
		print("Invalid input,please enter N for new game, X to exit game or L to view the Leaderboard")
		Selection=input("Enter Choice:")
	return Selection

def PrintIntro():
	print("\n",ThisUser.GetName(),", Welcome to Thousand Dollar Drop. You will start of with 1000 dollars and you play a set of 7 rounds. \n-In each round you shall choose any of the two topics available. \n-A question will then appear on the screen along with four other options. Now you shall choose how \n	much money you place in each option. \n-You shall input you answer in the form AA,BB,CC,DD , with each letter corresponding to its option \n	and remember, you can only put it in loads of 10s.\n-The money kept in the right option shall be carried forward to the next round, however you will \n	lose all the money which is kept on the incorrect option. \n-The game ends after 7 rounds or when you have 0 dollars left with you. :)")

def RandomIndex():
	ThisUser.GetPreviousTopic()
	RandomIndex1=random.randint(0,5)
	while RandomIndex1==ThisUser.GetPreviousTopic():
		RandomIndex1=random.randint(0,5)
	RandomIndex2=random.randint(0,5)
	while RandomIndex2==ThisUser.GetPreviousTopic() or RandomIndex2==RandomIndex1:
		RandomIndex2=random.randint(0,5)
	return (RandomIndex1,RandomIndex2)

def InputTopic(RandomIndex1,RandomIndex2):
	print("")
	print("CHOOSE YOUR TOPIC:  1.",ThisUser.GetTopic(RandomIndex1),"  2.",ThisUser.GetTopic(RandomIndex2))
	Topic=input("Select one of the 2 topics: ")
	while Topic!="1" and Topic!="2":
		Topic=input("	Please enter either 1 or 2: ")
	if Topic=="1":
		return (RandomIndex1)
	else: return (RandomIndex2)

def GetLine(NumberLine):
	File=open("EncryptedQuestions&Options.txt","r")
	for i in range(0,NumberLine):
		ThisLine= File.readline()
	return(ThisLine)
	File.close

def InputAnswer():
	print("\nYou have $", ThisUser.GetScore()," with you")
	AnswerChoice= str(input("\nEnter Answer: "))
	return (AnswerChoice)

def Validation(AnswerChoice):
	try:
		A,B,C,D=AnswerChoice.split(",")
		if int(A)<0 or int(B)<0 or int(C)<0 or int(D)<0:
			print("Please put a value above 0")
			return(False)
		elif int(A)%10!=0 or int(B)%10!=0 or int(C)%10!=0 or int(D)%10!=0:
			print("Please put amount in each option in multiples of 10")
			return(False)
		elif (int(A)+int(B)+int(C)+int(D))>ThisUser.GetScore():
			print("You have overspent. Please reduce",(int(A)+int(B)+int(C)+int(D))-ThisUser.GetScore())
			return(False)
		elif (int(A)+int(B)+int(C)+int(D))<ThisUser.GetScore():
			print("You have underspent. Please increase ", ThisUser.GetScore()-(int(A)+int(B)+int(C)+int(D)))
			return(False)
	except: 
		print("Please put in correct format")
		return (False)
	return(True)

def EnterScoreInLeaderboard():
	OpenLeaderboard=open("LeaderboardFile.txt","a")
	StrScore=str(ThisUser.GetScore())
	while len(StrScore)!=4:
		StrScore="0"+StrScore
	NameScore=StrScore+"_"+ThisUser.GetName()+"_"
	OpenLeaderboard.write(NameScore+"\n")
	OpenLeaderboard.close()
	return NameScore



#MAIN
LeaderboardList,StartPointer,FreeListPointer=CreateInitialLeaderboard()
Selection=Choice()

while Selection!="X" and Selection!="x":
	clear()
	if Selection=="N" or Selection=="n":
		N=input("Enter your Name:")
		ThisUser=User(N)
		PrintIntro()
		while ThisUser.GetRoundNo()!=8 and ThisUser.GetScore()!=0:
			Continue=input("Press enter to continue")
			clear()
			print(" ")
			print("---------------------------------------------Round ",ThisUser.GetRoundNo(),"---------------------------------------------")
			
			RandomIndex1, RandomIndex2= RandomIndex()
			TopicNo=InputTopic(RandomIndex1,RandomIndex2)
			ThisUser.SetPreviousTopic(TopicNo)
			LineNo=(TopicNo*20)+random.randint(1,20)
			Valid= ThisUser.NoQuestionsRepeated(LineNo)
			while Valid==False:
				LineNo=(TopicNo*20)+random.randint(1,20)
				Valid= ThisUser.NoQuestionsRepeated(LineNo)
			ThisLine=GetLine(LineNo)
			ThisQuestionAndOptions=QuestionAndOptions()
			ThisQuestionAndOptions.SetQuestionAndAnswers(ThisLine)

			AnswerIndex=ThisQuestionAndOptions.OutputRandomOrder()
			AnswerChoice=InputAnswer()
			IsAnswerValid=Validation(AnswerChoice)
			while IsAnswerValid!=True:
				AnswerChoice=InputAnswer()
				IsAnswerValid=Validation(AnswerChoice)
			ThisUser.SetScore(AnswerChoice,AnswerIndex)
			print("\n The Correct answer was ",ThisQuestionAndOptions.GetAnswer())
			print(" You now have $", ThisUser.GetScore()," to spend")
			ThisUser.IncrementRoundNo()
		print("--------------------------------------------------------GAME OVER--------------------------------------------------------")
		NameScore=EnterScoreInLeaderboard()
		InsertNode(LeaderboardList, StartPointer,FreeListPointer,NameScore)
		print("\n",ThisUser.GetName(), ", you finished the game with $" , ThisUser.GetScore()," left")
	elif Selection=="l" or Selection=="L":
		print("")
		PrintLeaderBoardList(LeaderboardList,StartPointer)
	Continue=input("Press enter to continue")
	clear()
	Selection=Choice()
print("PROGRAM IS OVER")	