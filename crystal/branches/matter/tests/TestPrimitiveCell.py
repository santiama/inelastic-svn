import unittest
from matter.Atom import Atom
from matter.Lattice import Lattice
from matter.Structure import Structure
class TestCase(unittest.TestCase):

    def test1(self):
        'Structure: property "primitive_unitcell"'
        lattice = Lattice(a=2,b=2,c=2,alpha=90,beta=90,gamma=90)
        atoms = [
            Atom('Ni', (0,0,0)),
            Atom('Ni', (0,0.5,0.5)),
            Atom('Ni', (0.5,0,0.5)),
            Atom('Ni', (0.5,0.5,0)),
            ]
        struct = Structure(lattice=lattice, atoms=atoms, sgid=225)
        pcell = struct.primitive_unitcell
        self.assert_(pcell)
        self.assertArrayEqual(
            pcell.base,
            [[-1., 0., 1.],
             [ 0., 1., 1.],
             [-1., 1., 0.]]
            )
        return


    def test2a(self):
        'Structure: methood "symConsistent"'
        lattice = Lattice(a=2,b=2,c=2,alpha=90,beta=90,gamma=90)
        atoms = [
            Atom('Ni', (0,0,0)),
            Atom('Ni', (0,0.5,0.5)),
            Atom('Ni', (0.5,0,0.5)),
            Atom('Ni', (0.5,0.5,0)),
            ]
        struct = Structure(lattice=lattice, atoms=atoms, sgid=225)
        verdict, pos, op = struct.symConsistent()
        self.assert_(verdict)
        return


    def test2b(self):
        'Structure: methood "symConsistent"'
        lattice = Lattice(a=2,b=2,c=2,alpha=90,beta=90,gamma=90)
        atoms = [
            Atom('Ni', (0,0,0)),
            Atom('Ni', (0,0.5,0.500000000000001)),
            Atom('Ni', (0.5,0,0.5)),
            Atom('Ni', (0.5,0.5,0)),
            ]
        struct = Structure(lattice=lattice, atoms=atoms, sgid=225)
        verdict, pos, op = struct.symConsistent()
        # print verdict, pos, op
        self.assert_(verdict)
        self.assert_(pos is None)
        self.assert_(op is None)
        return


    def test2c(self):
        'Structure: methood "symConsistent"'
        lattice = Lattice(a=2,b=2,c=2,alpha=90,beta=90,gamma=90)
        atoms = [
            Atom('Ni', (0,0,0)),
            Atom('Ni', (0,0.5,0.499999999999999)),
            Atom('Ni', (0.5,0,0.5)),
            Atom('Ni', (0.5,0.5,0)),
            ]
        struct = Structure(lattice=lattice, atoms=atoms, sgid=225)
        verdict, pos, op = struct.symConsistent()
        # print verdict, pos, op
        self.assert_(verdict)
        self.assert_(pos is None)
        self.assert_(op is None)
        return
        
    
    def test3(self):
        'Structure:  "primitive_unitcell"'
        lattice = Lattice(a=2,b=2,c=2,alpha=90,beta=90,gamma=90)
        atoms = [
            Atom('Fe', (0,0,0)),
            Atom('Pd', (0,0.5,0.5)),
            Atom('Pd', (0.5,0,0.5)),
            Atom('Pd', (0.5,0.5,0)),
            ]
        struct = Structure(lattice=lattice, atoms=atoms, sgid=221)
        verdict, pos, op = struct.symConsistent()
        # print verdict, pos, op
        self.assert_(verdict)
        self.assert_(pos is None)
        self.assert_(op is None)

        self.assertEqual(len(struct.primitive_unitcell.atoms), 4)
        return


    def assertArrayEqual(self, v1, v2):
        from numpy.testing import assert_array_almost_equal
        assert_array_almost_equal(v1, v2)
        return
        
    

def main():
    unittest.main()
    return



if __name__ == '__main__': main()
