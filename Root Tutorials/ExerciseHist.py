from ROOT import TFile, TCanvas, TH1D, TLegend, TChain
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



# Draw the histograms on the canvas, Aus Physics Tree nimmt man EIntries und füllt die Histogramme mit den Werten aus den Branches lep1_pt und lep2_pt.
physics_tree.Draw("lep1_pt >> hist_1")
physics_tree.Draw("lep2_pt >> hist_2", "", "sames") #sames generiert auch Statistik mit

#Aktuell überlagern sich beide Statistik-Boxen, man kann sie aber auch verschieben, wenn man möchte. (siehe unten)


#Statistiken Berechnen und ausgeben

# Für das erste Myon:
print(f"Leading muon pT: mean={pT_hist_1.GetMean():.6f}; rms={pT_hist_1.GetRMS():.6f}")
print(f"Leading muon pT integral: {pT_hist_1.Integral()}")

# Für das zweite Myon (genau dasselbe mit _2):
print(f"Subleading muon pT: mean={pT_hist_2.GetMean():.6f}; rms={pT_hist_2.GetRMS():.6f}")
print(f"Subleading muon pT integral: {pT_hist_2.Integral()}")


# Titel Umbennen (Eigentlich vom ersten Histogramm, da es das erste ist, das gezeichnet wird.)
pT_hist_1.SetTitle("Myon Transversalimpuls im Z-Boson Zerfall")


canvas.Update()  # Update the canvas to reflect changes

# Statistik-Boxen ausblenden, wenn man sie nicht sehen möchte
pT_hist_1.SetStats(False)  
pT_hist_2.SetStats(False) 
# Hier ausgeblendet, da man die Statistik-Boxen nicht sehen möchte. Man kann sie aber auch verschieben, wenn man möchte. (siehe unten)


# Mit dem Befehl python -i ExerciseHist.py kann man die Statistik-Boxen auch nachträglich noch verschieben und das PDF Speicher
# python -i öffnet Interaktives Fenster, wo man alles verschieben kann



#Legende erstellen, um die beiden Histogramme zu unterscheiden
legend = TLegend(0.66, 0.75, 0.86, 0.87)
legend.AddEntry(pT_hist_1, "Leading Lepton", "f")
legend.AddEntry(pT_hist_2, "Subleading Lepton", "f")
legend.SetBorderSize(1)
legend.Draw()


canvas.SetGrid(False,False) # Gridlines (x,y), bei (): x-Achse, y-Achse, beides
canvas.Draw()

# in vorherigem Ordner PDF Speichern
canvas.SaveAs("../PDFs/ExerciseHist.pdf")
