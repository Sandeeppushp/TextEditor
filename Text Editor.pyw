# install pyqt before running this file

import sys
from PyQt4 import QtGui, QtCore			

class window(QtGui.QMainWindow):
	def __init__(self):					#initial run when object created
		super(window,self).__init__()
		self.setGeometry(50,50,1100,640)
		self.setWindowTitle('Notepad by Sk')
		self.setWindowIcon(QtGui.QIcon('logo.png'))

		openEditor=QtGui.QAction('&Clear',self)
		openEditor.setShortcut('Ctrl+E')
		openEditor.setStatusTip('Open Editor')
		openEditor.triggered.connect(self.editor)

		openFile=QtGui.QAction('&Open File',self)
		openFile.setShortcut('Ctrl+O')
		openFile.setStatusTip('Open File')
		openFile.triggered.connect(self.file_open)

		saveFile=QtGui.QAction('&Save File',self)
		saveFile.setShortcut('Ctrl+S')
		saveFile.setStatusTip('Save File')
		saveFile.triggered.connect(self.file_save)



		self.statusBar()

		mainMenu=self.menuBar()
		fileMenu=mainMenu.addMenu('&File')								# set file name at menu bar

		fileMenu.addAction(openFile)
		fileMenu.addAction(saveFile)

		editorMenu=mainMenu.addMenu('&Clear')
		editorMenu.addAction(openEditor)


		self.home()

	def home(self):
		self.editor()
		extractAction=QtGui.QAction(QtGui.QIcon('file.png'),'flee the scene',self)
		extractAction.triggered.connect(self.close_application)


		self.show()

	def file_open(self):
		name=QtGui.QFileDialog.getOpenFileName(self,'Open File')
		file=open(name,'r')
		self.editor()
		with file:
			text=file.read()
			self.textEdit.setText(text)

	def file_save(self):
		name=QtGui.QFileDialog.getSaveFileName(self,'Save File')
		file=open(name,'w')
		text=self.textEdit.toPlainText()
		file.write(text)
		file.close()

	def editor(self):
		self.textEdit=QtGui.QTextEdit()
		self.setCentralWidget(self.textEdit)




	def close_application(self):
		choice=QtGui.QMessageBox.question(self,'Extract','Get into the chopper?',QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)
		if choice==QtGui.QMessageBox.Yes:
			print('Extracting Now')
			sys.exit()
		else:
			pass
		self.setWindowTitle('Title changed')




def run():
	app=QtGui.QApplication(sys.argv)
	GUI=window()
	sys.exit(app.exec_())
run()
