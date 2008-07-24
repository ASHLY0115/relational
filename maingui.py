# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created: Wed Jul 23 13:58:26 2008
#	  by: PyQt4 UI code generator 4.4.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import relation
import parser
import traceback
import sys

class Ui_Form(object):
	def __init__(self):
		self.relations={} #Dictionary for relations
	def execute(self):
		try:
			#Converting string to utf8 and then from qstring to normal string
			query=str(self.txtQuery.text().toUtf8())
			expr=parser.parse(query)
			print query, expr
			result=eval(expr,self.relations)
			
			res_rel=str(self.txtResult.text())#result relation's name
			if len(res_rel)==0:
				res_rel="last_"
				
			self.relations[res_rel]=result
			self.updateRelations()
			
			self.showRelation(result)
		except:
			print
			#QtGui.QMessageBox.information(None,QtGui.QApplication.translate("Form", "Error"),  str(traceback.print_exc()))
	def showRelation(self,rel):
		self.table.clear()
		
		for i in range(self.table.headerItem().columnCount()):
			self.table.headerItem().setText(i,"")
		
		if rel==None:
			self.table.headerItem().setText(0,"Empty relation")
			return
		
		for i in range(len(rel.header.attributes)):
			self.table.headerItem().setText(i,rel.header.attributes[i])
		
		for i in rel.content:
			item = QtGui.QTreeWidgetItem()
			for j in range(len(i)):
				item.setText(j, i[j])
			self.table.addTopLevelItem(item)
		
	def printRelation(self,*rel):
		for i in rel:
			self.showRelation(self.relations[str(i.text().toUtf8())])
			
	def showAttributes(self,*other):
		for i in other:
			rel=str(i.text().toUtf8())
			self.lstAttributes.clear()
			for j in self.relations[rel].header.attributes:
				self.lstAttributes.addItem (j)
			
	def updateRelations(self):
		self.lstRelations.clear()
		for i in self.relations:
			if i != "__builtin__":
			self.lstRelations.addItem(i)
	def unloadRelation(self):
		for i in self.lstRelations.selectedItems():
			del self.relations[i.text().toUtf8()]
		self.updateRelations()
	def showAbout(self):
		QtGui.QMessageBox.information(None,QtGui.QApplication.translate("Form", "About"),
		QtGui.QApplication.translate("Form", "Relational Algebra by Salvo 'LtWorf' Tomaselli", None, QtGui.QApplication.UnicodeUTF8))
	def loadRelation(self):
		res=QtGui.QInputDialog.getText(None, QtGui.QApplication.translate("Form", "New relation"),QtGui.QApplication.translate("Form", "Insert the name for the new relation"))
		if res[1]==False:
			return
		filename = QtGui.QFileDialog.getOpenFileName(None,QtGui.QApplication.translate("Form", "Load Relation"),"",QtGui.QApplication.translate("Form", "Relations (*.tlb);;Text Files (*.txt);;All Files (*)"))
		self.relations[str(res[0].toUtf8())]=relation.relation(filename)
		self.updateRelations()
		
	def addProduct(self):
		self.txtQuery.setText(self.txtQuery.text()+"*")
	def addDifference(self):
		self.txtQuery.setText(self.txtQuery.text()+u"-")
	def addUnion(self):
		self.txtQuery.setText(self.txtQuery.text()+u"ᑌ")
	def addIntersection(self):
		self.txtQuery.setText(self.txtQuery.text()+u"ᑎ")
	def addOLeft(self):
		self.txtQuery.setText(self.txtQuery.text()+u"ᐅLEFTᐊ")
	def addJoin(self):
		self.txtQuery.setText(self.txtQuery.text()+u"ᐅᐊ")
	def addORight(self):
		self.txtQuery.setText(self.txtQuery.text()+u"ᐅRIGHTᐊ")
	def addOuter(self):
		self.txtQuery.setText(self.txtQuery.text()+u"ᐅFULLᐊ")
	def addProjection(self):
		self.txtQuery.setText(self.txtQuery.text()+u"π")
	def addSelection(self):
		self.txtQuery.setText(self.txtQuery.text()+u"σ")
	def addRename(self):
		self.txtQuery.setText(self.txtQuery.text()+u"ρ")
	def addArrow(self):
		self.txtQuery.setText(self.txtQuery.text()+u"➡")
		
	def setupUi(self, Form):
		Form.setObjectName("Form")
		Form.resize(932,592)
		Form.setMinimumSize(QtCore.QSize(100,50))
		self.verticalLayout_7 = QtGui.QVBoxLayout(Form)
		self.verticalLayout_7.setObjectName("verticalLayout_7")
		self.horizontalLayout_4 = QtGui.QHBoxLayout()
		self.horizontalLayout_4.setObjectName("horizontalLayout_4")
		self.verticalLayout_4 = QtGui.QVBoxLayout()
		self.verticalLayout_4.setObjectName("verticalLayout_4")
		self.groupBox_4 = QtGui.QGroupBox(Form)
		self.groupBox_4.setObjectName("groupBox_4")
		self.verticalLayout_8 = QtGui.QVBoxLayout(self.groupBox_4)
		self.verticalLayout_8.setObjectName("verticalLayout_8")
		self.cmdAbout = QtGui.QPushButton(self.groupBox_4)
		self.cmdAbout.setObjectName("cmdAbout")
		self.verticalLayout_8.addWidget(self.cmdAbout)
		self.verticalLayout_4.addWidget(self.groupBox_4)
		self.groupBox = QtGui.QGroupBox(Form)
		self.groupBox.setObjectName("groupBox")
		self.verticalLayout_6 = QtGui.QVBoxLayout(self.groupBox)
		self.verticalLayout_6.setObjectName("verticalLayout_6")
		self.verticalLayout = QtGui.QVBoxLayout()
		self.verticalLayout.setObjectName("verticalLayout")
		self.cmdProduct = QtGui.QPushButton(self.groupBox)
		self.cmdProduct.setMaximumSize(QtCore.QSize(16777215,16777215))
		self.cmdProduct.setObjectName("cmdProduct")
		self.verticalLayout.addWidget(self.cmdProduct)
		self.cmdDifference = QtGui.QPushButton(self.groupBox)
		self.cmdDifference.setMaximumSize(QtCore.QSize(16777215,16777215))
		self.cmdDifference.setObjectName("cmdDifference")
		self.verticalLayout.addWidget(self.cmdDifference)
		self.cmdUnion = QtGui.QPushButton(self.groupBox)
		self.cmdUnion.setMaximumSize(QtCore.QSize(16777215,16777215))
		self.cmdUnion.setObjectName("cmdUnion")
		self.verticalLayout.addWidget(self.cmdUnion)
		self.cmdIntersection = QtGui.QPushButton(self.groupBox)
		self.cmdIntersection.setMaximumSize(QtCore.QSize(16777215,16777215))
		self.cmdIntersection.setObjectName("cmdIntersection")
		self.verticalLayout.addWidget(self.cmdIntersection)
		self.cmdJoin = QtGui.QPushButton(self.groupBox)
		self.cmdJoin.setMaximumSize(QtCore.QSize(16777215,16777215))
		self.cmdJoin.setObjectName("cmdJoin")
		self.verticalLayout.addWidget(self.cmdJoin)
		self.cmdOuterLeft = QtGui.QPushButton(self.groupBox)
		self.cmdOuterLeft.setMaximumSize(QtCore.QSize(16777215,16777215))
		self.cmdOuterLeft.setObjectName("cmdOuterLeft")
		self.verticalLayout.addWidget(self.cmdOuterLeft)
		self.cmdOuterRight = QtGui.QPushButton(self.groupBox)
		self.cmdOuterRight.setMaximumSize(QtCore.QSize(16777215,16777215))
		self.cmdOuterRight.setObjectName("cmdOuterRight")
		self.verticalLayout.addWidget(self.cmdOuterRight)
		self.cmdOuter = QtGui.QPushButton(self.groupBox)
		self.cmdOuter.setMaximumSize(QtCore.QSize(16777215,16777215))
		self.cmdOuter.setObjectName("cmdOuter")
		self.verticalLayout.addWidget(self.cmdOuter)
		self.cmdProjection = QtGui.QPushButton(self.groupBox)
		self.cmdProjection.setMaximumSize(QtCore.QSize(16777215,16777215))
		self.cmdProjection.setObjectName("cmdProjection")
		self.verticalLayout.addWidget(self.cmdProjection)
		self.cmdSelection = QtGui.QPushButton(self.groupBox)
		self.cmdSelection.setMaximumSize(QtCore.QSize(16777215,16777215))
		self.cmdSelection.setObjectName("cmdSelection")
		self.verticalLayout.addWidget(self.cmdSelection)
		self.cmdRename = QtGui.QPushButton(self.groupBox)
		self.cmdRename.setMaximumSize(QtCore.QSize(16777215,16777215))
		self.cmdRename.setObjectName("cmdRename")
		self.verticalLayout.addWidget(self.cmdRename)
		self.cmdArrow = QtGui.QPushButton(self.groupBox)
		self.cmdArrow.setMaximumSize(QtCore.QSize(16777215,16777215))
		self.cmdArrow.setObjectName("cmdArrow")
		self.verticalLayout.addWidget(self.cmdArrow)
		self.verticalLayout_6.addLayout(self.verticalLayout)
		self.verticalLayout_4.addWidget(self.groupBox)
		spacerItem = QtGui.QSpacerItem(20,40,QtGui.QSizePolicy.Minimum,QtGui.QSizePolicy.Expanding)
		self.verticalLayout_4.addItem(spacerItem)
		self.horizontalLayout_4.addLayout(self.verticalLayout_4)
		self.table = QtGui.QTreeWidget(Form) #QtGui.QTableView(Form)
		self.table.setAlternatingRowColors(True)
        	self.table.setRootIsDecorated(False)
		self.table.setObjectName("table")
		self.showRelation(None)
		self.horizontalLayout_4.addWidget(self.table)
		self.verticalLayout_3 = QtGui.QVBoxLayout()
		self.verticalLayout_3.setObjectName("verticalLayout_3")
		self.groupBox_2 = QtGui.QGroupBox(Form)
		self.groupBox_2.setMaximumSize(QtCore.QSize(200,16777215))
		self.groupBox_2.setObjectName("groupBox_2")
		self.verticalLayout_5 = QtGui.QVBoxLayout(self.groupBox_2)
		self.verticalLayout_5.setObjectName("verticalLayout_5")
		self.lstRelations = QtGui.QListWidget(self.groupBox_2)
		self.lstRelations.setMaximumSize(QtCore.QSize(300,16777215))
		self.lstRelations.setObjectName("lstRelations")
		self.verticalLayout_5.addWidget(self.lstRelations)
		self.cmdLoad = QtGui.QPushButton(self.groupBox_2)
		self.cmdLoad.setObjectName("cmdLoad")
		self.verticalLayout_5.addWidget(self.cmdLoad)
		self.cmdUnload = QtGui.QPushButton(self.groupBox_2)
		self.cmdUnload.setObjectName("cmdUnload")
		self.verticalLayout_5.addWidget(self.cmdUnload)
		self.verticalLayout_3.addWidget(self.groupBox_2)
		self.groupBox_3 = QtGui.QGroupBox(Form)
		self.groupBox_3.setMaximumSize(QtCore.QSize(200,16777215))
		self.groupBox_3.setObjectName("groupBox_3")
		self.horizontalLayout_6 = QtGui.QHBoxLayout(self.groupBox_3)
		self.horizontalLayout_6.setObjectName("horizontalLayout_6")
		self.lstAttributes = QtGui.QListWidget(self.groupBox_3)
		self.lstAttributes.setMaximumSize(QtCore.QSize(300,16777215))
		self.lstAttributes.setObjectName("lstAttributes")
		self.horizontalLayout_6.addWidget(self.lstAttributes)
		self.verticalLayout_3.addWidget(self.groupBox_3)
		self.horizontalLayout_4.addLayout(self.verticalLayout_3)
		self.verticalLayout_7.addLayout(self.horizontalLayout_4)
		self.horizontalLayout = QtGui.QHBoxLayout()
		self.horizontalLayout.setObjectName("horizontalLayout")
		self.label = QtGui.QLabel(Form)
		self.label.setObjectName("label")
		self.horizontalLayout.addWidget(self.label)
		self.txtResult = QtGui.QLineEdit(Form)
		self.txtResult.setMaximumSize(QtCore.QSize(70,16777215))
		self.txtResult.setObjectName("txtResult")
		self.horizontalLayout.addWidget(self.txtResult)
		self.label_2 = QtGui.QLabel(Form)
		self.label_2.setObjectName("label_2")
		self.horizontalLayout.addWidget(self.label_2)
		self.txtQuery = QtGui.QLineEdit(Form)
		self.txtQuery.setObjectName("txtQuery")
		self.horizontalLayout.addWidget(self.txtQuery)
		self.cmdExecute = QtGui.QPushButton(Form)
		self.cmdExecute.setAutoDefault(False)
		self.cmdExecute.setDefault(True)
		self.cmdExecute.setFlat(False)
		self.cmdExecute.setObjectName("cmdExecute")
		self.horizontalLayout.addWidget(self.cmdExecute)
		self.verticalLayout_7.addLayout(self.horizontalLayout)
		self.label.setBuddy(self.txtResult)
		self.label_2.setBuddy(self.txtQuery)

		self.retranslateUi(Form)
		QtCore.QObject.connect(self.cmdAbout,QtCore.SIGNAL("clicked()"),self.showAbout)
		QtCore.QObject.connect(self.cmdProduct,QtCore.SIGNAL("clicked()"),self.addProduct)
		QtCore.QObject.connect(self.cmdDifference,QtCore.SIGNAL("clicked()"),self.addDifference)
		QtCore.QObject.connect(self.cmdUnion,QtCore.SIGNAL("clicked()"),self.addUnion)
		QtCore.QObject.connect(self.cmdIntersection,QtCore.SIGNAL("clicked()"),self.addIntersection)
		QtCore.QObject.connect(self.cmdOuterLeft,QtCore.SIGNAL("clicked()"),self.addOLeft)
		QtCore.QObject.connect(self.cmdJoin,QtCore.SIGNAL("clicked()"),self.addJoin)
		QtCore.QObject.connect(self.cmdOuterRight,QtCore.SIGNAL("clicked()"),self.addORight)
		QtCore.QObject.connect(self.cmdOuter,QtCore.SIGNAL("clicked()"),self.addOuter)
		QtCore.QObject.connect(self.cmdProjection,QtCore.SIGNAL("clicked()"),self.addProjection)
		QtCore.QObject.connect(self.cmdSelection,QtCore.SIGNAL("clicked()"),self.addSelection)
		QtCore.QObject.connect(self.cmdRename,QtCore.SIGNAL("clicked()"),self.addRename)
		QtCore.QObject.connect(self.cmdArrow,QtCore.SIGNAL("clicked()"),self.addArrow)
		QtCore.QObject.connect(self.cmdExecute,QtCore.SIGNAL("clicked()"),self.execute)
		QtCore.QObject.connect(self.cmdLoad,QtCore.SIGNAL("clicked()"),self.loadRelation)
		QtCore.QObject.connect(self.cmdUnload,QtCore.SIGNAL("clicked()"),self.unloadRelation)
		QtCore.QObject.connect(self.lstRelations,QtCore.SIGNAL("itemDoubleClicked(QListWidgetItem*)"),self.printRelation)
		QtCore.QObject.connect(self.lstRelations,QtCore.SIGNAL("itemActivated(QListWidgetItem*)"),self.showAttributes)
		QtCore.QMetaObject.connectSlotsByName(Form)
		Form.setTabOrder(self.	txtResult,self.txtQuery)
		Form.setTabOrder(self.txtQuery,self.cmdExecute)
		Form.setTabOrder(self.cmdExecute,self.lstRelations)
		Form.setTabOrder(self.lstRelations,self.cmdLoad)
		Form.setTabOrder(self.cmdLoad,self.cmdUnload)
		Form.setTabOrder(self.cmdUnload,self.lstAttributes)
		Form.setTabOrder(self.lstAttributes,self.table)
		Form.setTabOrder(self.table,self.cmdProduct)
		Form.setTabOrder(self.cmdProduct,self.cmdUnion)
		Form.setTabOrder(self.cmdUnion,self.cmdJoin)
		Form.setTabOrder(self.cmdJoin,self.cmdOuterLeft)
		Form.setTabOrder(self.cmdOuterLeft,self.cmdProjection)
		Form.setTabOrder(self.cmdProjection,self.cmdRename)
		Form.setTabOrder(self.cmdRename,self.cmdAbout)

	def retranslateUi(self, Form):
		Form.setWindowTitle(QtGui.QApplication.translate("Form", "Relational", None, QtGui.QApplication.UnicodeUTF8))
		self.groupBox_4.setTitle(QtGui.QApplication.translate("Form", "Menu", None, QtGui.QApplication.UnicodeUTF8))
		self.cmdAbout.setText(QtGui.QApplication.translate("Form", "About", None, QtGui.QApplication.UnicodeUTF8))
		self.groupBox.setTitle(QtGui.QApplication.translate("Form", "Operators", None, QtGui.QApplication.UnicodeUTF8))
		self.cmdProduct.setToolTip(QtGui.QApplication.translate("Form", "Product operator", None, QtGui.QApplication.UnicodeUTF8))
		self.cmdProduct.setText(QtGui.QApplication.translate("Form", "*", None, QtGui.QApplication.UnicodeUTF8))
		self.cmdDifference.setToolTip(QtGui.QApplication.translate("Form", "Difference operator", None, QtGui.QApplication.UnicodeUTF8))
		self.cmdDifference.setText(QtGui.QApplication.translate("Form", "-", None, QtGui.QApplication.UnicodeUTF8))
		self.cmdUnion.setToolTip(QtGui.QApplication.translate("Form", "Union operator", None, QtGui.QApplication.UnicodeUTF8))
		self.cmdUnion.setText(QtGui.QApplication.translate("Form", "ᑌ", None, QtGui.QApplication.UnicodeUTF8))
		self.cmdIntersection.setToolTip(QtGui.QApplication.translate("Form", "Intersection operator", None, QtGui.QApplication.UnicodeUTF8))
		self.cmdIntersection.setText(QtGui.QApplication.translate("Form", "ᑎ", None, QtGui.QApplication.UnicodeUTF8))
		self.cmdJoin.setToolTip(QtGui.QApplication.translate("Form", "Natural join operator", None, QtGui.QApplication.UnicodeUTF8))
		self.cmdJoin.setText(QtGui.QApplication.translate("Form", "ᐅᐊ", None, QtGui.QApplication.UnicodeUTF8))
		self.cmdOuterLeft.setToolTip(QtGui.QApplication.translate("Form", "Outer join left operator", None, QtGui.QApplication.UnicodeUTF8))
		self.cmdOuterLeft.setText(QtGui.QApplication.translate("Form", "ᐅLEFTᐊ", None, QtGui.QApplication.UnicodeUTF8))
		self.cmdOuterRight.setToolTip(QtGui.QApplication.translate("Form", "Outer join right operator", None, QtGui.QApplication.UnicodeUTF8))
		self.cmdOuterRight.setText(QtGui.QApplication.translate("Form", "ᐅRIGHTᐊ", None, QtGui.QApplication.UnicodeUTF8))
		self.cmdOuter.setToolTip(QtGui.QApplication.translate("Form", "Outer join full operator", None, QtGui.QApplication.UnicodeUTF8))
		self.cmdOuter.setText(QtGui.QApplication.translate("Form", "ᐅFULLᐊ", None, QtGui.QApplication.UnicodeUTF8))
		self.cmdProjection.setToolTip(QtGui.QApplication.translate("Form", "Projection operator", None, QtGui.QApplication.UnicodeUTF8))
		self.cmdProjection.setText(QtGui.QApplication.translate("Form", "π", None, QtGui.QApplication.UnicodeUTF8))
		self.cmdSelection.setToolTip(QtGui.QApplication.translate("Form", "Selection operator", None, QtGui.QApplication.UnicodeUTF8))
		self.cmdSelection.setText(QtGui.QApplication.translate("Form", "σ", None, QtGui.QApplication.UnicodeUTF8))
		self.cmdRename.setToolTip(QtGui.QApplication.translate("Form", "Rename operator", None, QtGui.QApplication.UnicodeUTF8))
		self.cmdRename.setText(QtGui.QApplication.translate("Form", "ρ", None, QtGui.QApplication.UnicodeUTF8))
		self.cmdArrow.setToolTip(QtGui.QApplication.translate("Form", "Rename attribute", None, QtGui.QApplication.UnicodeUTF8))
		self.cmdArrow.setText(QtGui.QApplication.translate("Form", "➡", None, QtGui.QApplication.UnicodeUTF8))
		self.groupBox_2.setTitle(QtGui.QApplication.translate("Form", "Relations", None, QtGui.QApplication.UnicodeUTF8))
		self.lstRelations.setToolTip(QtGui.QApplication.translate("Form", "List all the relations.\n"
"Double click on a relation to show it in the table.", None, QtGui.QApplication.UnicodeUTF8))
		self.cmdLoad.setWhatsThis(QtGui.QApplication.translate("Form", "Loads a relation from a file", None, QtGui.QApplication.UnicodeUTF8))
		self.cmdLoad.setText(QtGui.QApplication.translate("Form", "Load relation", None, QtGui.QApplication.UnicodeUTF8))
		self.cmdUnload.setToolTip(QtGui.QApplication.translate("Form", "Unloads a relation", None, QtGui.QApplication.UnicodeUTF8))
		self.cmdUnload.setText(QtGui.QApplication.translate("Form", "Unload relation", None, QtGui.QApplication.UnicodeUTF8))
		self.groupBox_3.setTitle(QtGui.QApplication.translate("Form", "Attributes", None, QtGui.QApplication.UnicodeUTF8))
		self.lstAttributes.setToolTip(QtGui.QApplication.translate("Form", "Shows the attributes of the current relation", None, QtGui.QApplication.UnicodeUTF8))
		self.label.setText(QtGui.QApplication.translate("Form", "Query", None, QtGui.QApplication.UnicodeUTF8))
		self.label_2.setText(QtGui.QApplication.translate("Form", "=", None, QtGui.QApplication.UnicodeUTF8))
		self.cmdExecute.setText(QtGui.QApplication.translate("Form", "Execute", None, QtGui.QApplication.UnicodeUTF8))


if __name__ == "__main__":
	import sys
	app = QtGui.QApplication(sys.argv)
	Form = QtGui.QWidget()
	
	ui = Ui_Form()
	ui.setupUi(Form)
	Form.show()
	Form.setWindowTitle("Relational")
	sys.exit(app.exec_())

