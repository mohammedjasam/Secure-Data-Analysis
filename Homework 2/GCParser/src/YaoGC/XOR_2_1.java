// Copyright (C) 2010 by Yan Huang <yhuang@virginia.edu>

package YaoGC;

import java.math.*;

import Utils.*;

public class XOR_2_1 extends SimpleCircuit_2_1 {
    public XOR_2_1() {
	super("XOR_2_1");
    }

    protected void compute() {
	int left  = inputWires[0].value;
	int right = inputWires[1].value;

	outputWires[0].value = left ^ right;
    }

    public void execute() {
	Wire inWireL = inputWires[0];
	Wire inWireR = inputWires[1];
	Wire outWire = outputWires[0];

	if (inWireL.value != Wire.UNKNOWN_SIG && inWireR.value != Wire.UNKNOWN_SIG) {
	    compute();
	}
	else if (inWireL.value != Wire.UNKNOWN_SIG) {
	    if (inWireL.value == 0)
		outWire.invd = inWireR.invd;
	    else
		outWire.invd = !inWireR.invd;

	    outWire.value = Wire.UNKNOWN_SIG;
	    outWire.setLabel(inWireR.lbl);
	}
	else if (inWireR.value != Wire.UNKNOWN_SIG) {
	    if (inWireR.value == 0)
		outWire.invd = inWireL.invd;
	    else
		outWire.invd = !inWireL.invd;

	    outWire.value = Wire.UNKNOWN_SIG;
	    outWire.setLabel(inWireL.lbl);
	}
	else {
	    if (collapse()) {

	    }
	    else {
		BigInteger l = inWireL.lbl;
		BigInteger r = inWireR.lbl;
	
		BigInteger out = l.xor(r);
	
		outWire.invd = inWireL.invd ^ inWireR.invd;
		outWire.value = Wire.UNKNOWN_SIG;
		outWire.setLabel(out);
	    }
	}

	// System.out.print("XOR: " + Color.blue);
	// if (inWireL.value == Wire.UNKNOWN_SIG) 
	//     System.out.print("(" + 
	// 		     ((!inWireL.invd) ? 
	// 		      (inWireL.lbl + ", " + Wire.conjugate(inWireL.lbl)) :
	// 		      (Wire.conjugate(inWireL.lbl) + ", " + inWireL.lbl))
	// 		     + ") XOR ");
	// else
	//     System.out.print(inWireL.value + " XOR ");

	// if (inWireR.value == Wire.UNKNOWN_SIG)
	//     System.out.print("(" + 
	// 		     ((!inWireR.invd) ? 
	// 		      (inWireR.lbl + ", " + Wire.conjugate(inWireR.lbl)) :
	// 		      (Wire.conjugate(inWireR.lbl) + ", " + inWireR.lbl))
	// 		     + ") = ");
	// else
	//     System.out.print(inWireR.value + " = ");

	// if (outWire.value == Wire.UNKNOWN_SIG)
	//     System.out.print("(" + 
	// 		     ((!outWire.invd) ? 
	// 		      (outWire.lbl + ", " + Wire.conjugate(outWire.lbl)) :
	// 		      (Wire.conjugate(outWire.lbl) + ", " + outWire.lbl))
	// 		     + ").");
	// else
	//     System.out.print(outWire.value + ".");
	// System.out.println(Color.black);

	outWire.setReady();
    }

    protected boolean collapse() {
    	Wire inWireL = inputWires[0];
    	Wire inWireR = inputWires[1];
    	Wire outWire = outputWires[0];

    	if (inWireL.lbl.equals(inWireR.lbl)) {
    	    if (inWireL.invd == inWireR.invd) {
    		outWire.invd = false;
    		outWire.value = 0;
    	    }
    	    else {
    		outWire.invd = false;
    		outWire.value = 1;
    	    }

    	    return true;
    	}

    	return false;
    }

    // Never used for XOR gate.
    protected boolean shortCut() {return false;}
    // Never used for XOR gate.
    protected void fillTruthTable() {}
    protected void execYao() {}
}
