from ROOT import TFile, TCanvas, TH1D, TChain
import ROOT

#Damit man mit Setfillcoloralpha arbeiten kann, muss man die OpenGL-Option aktivieren. (also für Transparentes Zeichnen)
ROOT.gStyle.SetCanvasPreferGL(True)

#Open the Zmumu.root file and load the physics tree
Zmumu_file = TFile("Zmumu.root")
physics_tree = Zmumu_file.Get("physics")


#Or
#physics_tree = TChain("physics")
#physics_tree.Add("Zmumu.root")
#Check number of events
N_events = physics_tree.GetEntries()
print(f'NEvents: {N_events}')


#Create two histograms with 40 bins ranging from 0 to 200 to plot the transverse momentum (pt) of the muons
pT_hist_1 = TH1D("hist_1", "Leading lepton pT", 70, 0, 200)
pT_hist_2 = TH1D("hist_2", "Subleading lepton pT", 70, 0, 200)



#Set histogram colors
pT_hist_1.SetFillColorAlpha(2, 0.7)
pT_hist_2.SetFillColorAlpha(4, 0.3)


# Achsen zuweisen
pT_hist_1.GetXaxis().SetTitle("Transverse Momentum [GeV]")
pT_hist_1.GetYaxis().SetTitle("Counts")

# --- HIER DEN ABSTAND ANPASSEN ---
pT_hist_1.GetXaxis().SetTitleOffset(1.3)  
pT_hist_1.GetYaxis().SetTitleOffset(1.3)  

# Achsen zentrieren
pT_hist_1.GetXaxis().CenterTitle(True)  
pT_hist_1.GetYaxis().CenterTitle(True)


#Create a canvas and Fill the histograms with leading and subleading muon pt from branches lep1_pt and lep2_pt
# You can draw them on the same canvas of different canvases. Here, they are drawn on the same canvas.

canvas = TCanvas()#("canvas", "", 800, 600)

physics_tree.Draw("lep1_pt >> hist_1")



physics_tree.Draw("lep2_pt >> hist_2", "", "same")

canvas.Draw()

# in vorherigem Ordner PDF Speichern
canvas.SaveAs("../PDFs/ExerciseHist.pdf")
