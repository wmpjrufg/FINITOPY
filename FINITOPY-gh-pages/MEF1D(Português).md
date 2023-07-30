<h1>MEF 1D</h1>

<p align="justify">Nesta seção são apresentados as funções da biblioteca MEF1D da plataforma FINITOpy.</p>

<code>GET_VALUE_FROM_TXT_MEF1D_FINITO</code>

<dl>
    <dt>Entrada de dados</dt>
      <dd>
          <table>
          <thead>
          <tr>
              <th>Variável</th>
              <th>Descrição</th>
              <th>Tipo</th>
          </tr>
          </thead>
          <tbody>
          <tr>
              <td>Nome do arquivo</td>
              <td>Dataset Estrutural</td>
              <td>.txt</td>
          </tr>
          </tbody>
          </table>
      </dd>
      <dt>Saída de dados</dt>
      <dd>
        <table>
        <thead>
        <tr>
          <th>Variáveis</th>
          <th>Descrição</th>
          <th>Tipo</th>
        </tr>
        </thead>
        <tbody>
        <tr>
          <td>TYPE_ELEMENT</td>
          <td>Tipo de elemento em algoritmo Finito<br>0: Frame bar element</td>
          <td>Inteira</td>
        </tr>
        <tr>
          <td>TYPE_SOLUTION</td>
          <td>Solution of the system of equations<br>0: Condense procedure<br>1: Zero and One algorithm</td>
          <td>Inteira</td>
        </tr>
        </tbody>
         <tr>
          <td>N_NODES</td>
          <td>Number of nodes</td>
          <td>Inteira</td>
        </tr>
         <tr>
          <td>N_MATERIALS</td>
          <td>Number of materials</td>
          <td>Inteira</td>
        </tr>
         <tr>
          <td>N_SECTIONS</td>
          <td>Number of sections</td>
          <td>Inteira</td>
        </tr>
         <tr>
          <td>N_ELEMENTS</td>
          <td>Number of flame elements</td>
          <td>Inteira</td>
        </tr>
         <tr>
          <td>N_DOFPRESCRIPTIONS</td>
          <td>Number of DOF displacement control</td>
          <td>Inteira</td>
        </tr>
         <tr>
          <td>N_DOFLOADED</td>
          <td>Number of DOF forces</td>
          <td>Inteira</td>
        </tr>
         <tr>
          <td>N_DOSPRINGS</td>
          <td>Number of DOF spring elements</td>
          <td>Inteira</td>
        </tr>
        <tr>
          <td>COORDINATES</td>
          <td>Coordinates properties<br><br></td>
          <td>Matriz por Numpy</td>
        </tr>
        <tr>
          <td>COORDINATES</td>
          <td>Coordinates properties<br>Node, x, y<br></td>
          <td>Matriz por Numpy</td>
        </tr>
        <tr>
          <td>ELEMENTS</td>
          <td>Elements properties<br>Node 0 ...<br>Node (N_NODES - 1)<br>Geometry ID<br>HInge ID node 0<br>HInge ID node 1<br></td>
          <td>Matriz por Numpy</td>
        </tr>
        <tr>
          <td>MATERIALS</td>
          <td>Materials proprieties<br>Young<br>Poisson<br>Density<br>Thermal coefficient<br>Sections proprieties</td>
          <td>Matriz por Numpy</td>
        </tr>
        <tr>
          <td>SECTIONS</td>
          <td>Sections proprieties<br>Area<br>Density<br>Inercia Flame Bar<br>X GC<br>Y CG</td>
          <td>Matriz por Numpy</td>
        </tr>
        <tr>
          <td>PRESCRIPTIONS</td>
          <td>Propriedades das seções<br>Área<br>Densidade<br>Inercia da barra<br>X GC<br>Y CG</td>
          <td>Matriz por Numpy</td>
        </tr>
        <tr>
          <td>NODAL_LOAD</td>
          <td>Node<br>Direcion(X=0,Y=1,Z=2)<br>
          Value</td>
          <td>Matriz por Numpy</td>
        </tr>
        <tr>
          <td>SPRINGS</td>
          <td>Node<br>Direcion(X=0,Y=1,Z=2)<br>
          Value</td>
          <td>Matriz por Numpy</td>
        </tr>
        </table>
      </dd>  
</dl>

<code>GET_VALUE_FROM_DICT_MEF1D_FINITO</code>

<p align="justify"> Esta Função Lê dados do dicionário.</p>

<dl>
    <dt>Entrada de dados:</dt>
      <dd>
          <table>
          <thead>
          <tr>
              <th>Variáveis</th>
              <th>Descrição</th>
              <th>Tipo</th>
          </tr>
          </thead>
          <tbody>
          <tr>
              <td>Dicionário</td>
              <td>Dataset Estrutural</td>
              <td>Pelo Dicionário</td>
          </tr>
          </tbody>
          </table>
      </dd>
      <dt>Saída de dados:<dt>
      <dd>
          <table>
          <thead>
          <tr>
              <th>Variável</th>
              <th>Descrição</th>
              <th>Tipo</th>
          </tr>
          </thead>
          <tbody>
          <tr>
              <td>TYPE_ELEMENT</td>
              <td>Digita o elemento no algoritmo finito <br>0 - Frame bar element</td>
              <td>Inteiro</td>
          </tr>
          <tr>
              <td>TYPE_SOLUTION</td>
              <td>Solução de sistemas de equações
               <br>0 - Processo de condensação<br>1 - Algoritmo Zero e Um</td>
              <td>Inteiro</td>
          </tr>
          <tr>
              <td>TYPE_SOLUTION</td>
              <td>Solução de sistema de equações <br>0 - processo de condensação<br>1 - Algoritmo Zero e Um</td>
              <td>Inteiro</td>
          </tr>
          <tr>
              <td>N_NODES</td>
              <td>Número de nós</td>
              <td>Inteiro</td>
          </tr>
          <tr>
              <td>N_MATERIALS</td>
              <td>Número de materiais</td>
              <td>Inteiro</td>
          </tr>
          <tr>
              <td>N_SECTIONS</td>
              <td>Número de seções</td>
              <td>Inteiro</td>
          </tr>
          <tr>
              <td>N_ELEMENTES</td>
              <td>Número de Elementos</td>
              <td>Inteiro</td>
          </tr>
          <tr>
              <td>N_DOFPRESCRIPTIONS</td>
              <td>Número de DOF displacement control</td>
              <td>Inteiro</td>
          </tr>
          <tr>
              <td>N_DOFLOADED</td>
              <td>Número de  DOF forces</td>
              <td>Inteiro</td>
          </tr>
          <tr>
              <td>N_DOSPRINGS</td>
              <td>Número de DOF spring elements</td>
              <td>Inteiro</td>
          </tr>
          <tr>
              <td>COORDINATES</td>
              <td>Propriedades das coordenadas<br>Node x,y</td>
              <td>Por Matriz Numpy</td>
          </tr>
          <tr>
              <td>ELEMENTS</td>
              <td>Propriedades dos elementos<br>Node 0 ...<br>Node (N_NODES -1)<br>Hinge ID node 1</td>
              <td>Py Numpy Array</td>
          </tr>
          <tr>
              <td>MATERIALS</td>
              <td>Propriedades dos materiais<br>Young<br>Poisson<br>Density<br>Thermal Coefficient
              </td>
              <td>Matriz por Numpy</td>
          </tr>
          <tr>
              <td>SECTIONS</td>
              <td>Propriedades das seções<br>Area<br>Inertia 1<br>Inertia Flame bar<br>X GC<br>Y GC
              </td>
              <td>Py Numpy Array</td>
          </tr>
          <tr>
              <td>PRESCRIPTIONS</td>
              <td>Propriedades de deslocamento prescritas<br>Node<br>Direcion(X=0,Y=1,Z=2)<br>Value Nodal DOF force properties
              </td>
              <td>Matriz por Numpy</td>
          </tr>
          <tr>
              <td>PRESCRIPTIONS</td>
              <td>Propriedades de deslocamentos DOF prescritos<br>Node<br>Direcion(X=0,Y=1,Z=2)<br>Value Nodal DOF force properties
              </td>
              <td>Matriz por Numpy</td>
          </tr>
          <tr>
              <td>NODAL_LOAD</td>
              <td>Nodal DOF force properties<br>Node<br>Direcion(X=0,Y=1,Z=2)<br>Value Nodal DOF spring properties
              </td>
              <td>Matriz por Numpy</td>
          </tr>
          <tr>
              <td>SPRINGS</td>
              <td>Nodal DOF force properties<br>Node<br>Direcion(X=0,Y=1,Z=2)<br>Value
              </td>
              <td>Matriz por numpy</td>
          </tr>
        </table>
        </dd>
</dl>


<code>MATERIALS_PROPERTIES0</code>

<p align="justify"> Esta função cria um vetor com um material de informação I_ELEMENT e TYPE_ELEMENT = 0.</p>


<d1>Entrada de dados:</dt>
      <dd>
          <table>
          <thead>
          <tr>
              <th>Variáveis</th>
              <th>Descrição</th>
              <th>Tipo</th>
          </tr>
          </thead>
          <tbody>
          <tr>
              <td>ELEMENTS PROPERTIES</td>
              <td>ID, NOde 0... Node (N_NODES - 1), Material ID, Geomertry ID, Hinge ID node 1, Hinge ID node 2</td>
              <td>Matriz por Numpy</td>
          </tr>
          </tbody>
          </table>
      </dd> 
    <dt>Saída de dados:</dt>
      <dd>
          <table>
          <thead>
          <tr>
              <th>Variáveis</th>
              <th>Descrição</th>
              <th>Tipo</th>
          </tr>
          </thead>
          <tbody>
          <tr>
              <td>MATERIAL_iELEMENT</td>
              <td>Material I_ELEMENT properties<br>[0] - Young<br>[1] - Shear modulos<br>[3] - Thermal coefficient<br>[4] - Density</td>
              <td>Py numpy Array</td>
          </tr>
          </tbody>
          </table>
        </dd>    
<d1>



<code>GEOMETRIC_PROPERTIES0</code>

<p align="justify"> Esta Função atribuí propriedades geométricas a barra de I_ELEMENT element TYPE_ELEMENT = 0 (Frame element).</p>


<d1>
    <dt>Entrada de dados:</dt>
      <dd>
          <table>
          <thead>
          <tr>
              <th>Variáveis</th>
              <th>Descrição</th>
              <th>Tipo</th>
          </tr>
          </thead>
          <tbody>
          <tr>
              <td>ELEMENTS PROPERTIES</td>
              <td>ID, NOde 0... Node (N_NODES - 1), Material ID, Geomertry ID, Hinge ID node 1, Hinge ID node 2</td>
              <td>Matriz por Numpy</td>
          </tr>
          <tr>
              <td>COORDENADAS</td>
              <td>PROPRIEDADES DAS COORDENADAS<br> Node, x, y</td>
              <td>Matriz por numpy</td>
          </tr>
          <tr>
              <td>Propriedades de Elementos</td>
              <td>Propriedades de elementos<br> Node (N_NODES - 1), Mateiral ID, Geometry ID, Hinge ID node 1, Hinge ID node 2,</td>
              <td>Matriz por numpy</td>
          </tr>
          <tr>
              <td>SECTIONS</td>
              <td>Propriedades dos Elementos<br>Area, Inertia 1,
              Inertia Flame bar, X GC, Y GC</td>
              <td>Matriz por numpy</td>
          </tr>
          <tr>
              <td>AUX_2</td>
              <td>ID section</td>
              <td>Inteira</td>
          </tr>
          <tr>
              <td>I_ELEMENT</td>
              <td>i elemento em looping</td>
              <td>Inteira</td>
          </tr>
          </tbody>
          </table>
      </dd> 
    <dt>Saída de dados:</dt>
      <dd>
          <table>
          <thead>
          <tr>
              <th>Variável</th>
              <th>descrição</th>
              <th>Tipo</th>
          </tr>
          </thead>
          <tbody>
          <tr>
              <td>SECTION_IELEMENT</td>
              <td>Propriedades de I_ELEMENT seções<br>[0] - Length<br>[1] - Sine<br>[2] - Consine<br>[3] - Area<br>[4] - Inertia auxiliar<br>[5] - Inertia Flame element</td>
              <td>Py loest[6]</td>
          </tr>
          </tbody>
          </table>
        </dd>    
<d1>

<code>HINGED_PROPERTIES0</code>

<p align="justify"> Esta função cria um array com hinge properties per node.</p>


<d1>
    <dt>Entrada de dados:</dt>
      <dd>
          <table>
          <thead>
          <tr>
              <th>Variáveis</th>
              <th>Descrição</th>
              <th>Tipo</th>
          </tr>
          </thead>
          <tbody>
          <tr>
              <td>ELEMENTS PROPERTIES</td>
              <td>ID, NOde 0... Node (N_NODES - 1), Material ID, Geomertry ID, Hinge ID node 1, Hinge ID node 2</td>
              <td>Py numpy Array</td>
          </tr>
          </tbody>
          </table>
      </dd> 
    <dt>Saída de dados:</dt>
      <dd>
          <table>
          <thead>
          <tr>
              <th>Variáveis</th>
              <th>Descrição</th>
              <th>Tipo</th>
          </tr>
          </thead>
          <tbody>
          <tr>
              <td>HINGES</td>
              <td>Propriedades de hinge por nó<br>[0] - No hinge<br>[1] - Yes hinge</td>
              <td>Matriz por Numpy</td>
          </tr>
          </tbody>
          </table>
        </dd>    
<d1>



<code>ELEMENT_STIFFINESS_0</code>

<p align="justify"> This function creates the element stiffness matrix of the I_ELEMENT.</p>


<d1>
    <dt>Input:</dt>
      <dd>
          <table>
          <thead>
          <tr>
              <th>Variable</th>
              <th>About</th>
              <th>Type</th>
          </tr>
          </thead>
          <tbody>
          <tr>
              <td>TYPE_ELEMENT</td>
              <td>Type element in Finite algorithm<br>0 - Flame bar element</td>
              <td>Integer</td>
          </tr>
          <tr>
              <td>SECTION_IELEMENT</td>
              <td>Section I_ELEMENT properties<br>[0] - Length<br>[1] - Sine<br>[2] - Cosine<br>[3] - Area<br>[4] - Inertia auxiliar<br>[5] - Inertia Flame element</td>
              <td>Integer</td>
          </tr>
          <tr>
              <td>MATERIAL_IELEMENT</td>
              <td>Material I_ELEMENT properties<br>[0] - Young<br>[1] - Shear modulos<br>[2] - Poisson<br>[3] - Thermal Coefficient<br>[4] - Density</td>
              <td>Py list[5]</td>
          </tr>
          <tr>
              <td>HINGES</td>
              <td>Hinge properties per node<br>0 - No hinge<br>1 - Yes hinge</td>
              <td>Py Numpy array[N_NODESx2]</td>
          </tr>
          </tbody>
          </table>
      </dd> 
    <dt>Output:</dt>
      <dd>
          <table>
          <thead>
          <tr>
              <th>Variable</th>
              <th>about</th>
              <th>Type</th>
          </tr>
          </thead>
          <tbody>
          <tr>
              <td>K_IELEMENT</td>
              <td>Local stiffness matrix I_ELEMENT</td>
              <td>Py Numpy Array [N_DOFELEMET X N_DOFSELEMENT]</td>
          </tr>
          </tbody>
          </table>
        </dd>    
<d1>


<code>ELEMENT_ROTATION</code>

<p align="justify"> This function creates the rotation matrix of the I_ELEMENT element.</p>


<d1>
    <dt>Input:</dt>
      <dd>
          <table>
          <thead>
          <tr>
              <th>Variable</th>
              <th>About</th>
              <th>Type</th>
          </tr>
          </thead>
          <tbody>
          <tr>
              <td>TYPE_ELEMENT</td>
              <td>Type element in Finite algorithm<br>0 - Flame bar element</td>
              <td>Integer</td>
          </tr>
          <tr>
              <td>SECTION_IELEMENT</td>
              <td>Section I_ELEMENT properties<br>[0] - Length<br>[1] - Sine<br>[2] - Cosine<br>[3] - Area<br>[4] - Inertia auxiliar<br>[5] - Inertia Flame element</td>
              <td>Py list [6]</td>
          </tr>
          <tr>
              <td>R_IELEMENT</td>
              <td>ROtation Matrix I_ELEMENT<br>0 - No hinge<br>1 - Yes hinge</td>
              <td>Py Numpy array[N_NODESx2]</td>
          </tr>
          </tbody>
          </table>
      </dd> 
    <dt>Output:</dt>
      <dd>
          <table>
          <thead>
          <tr>
              <th>Variable</th>
              <th>about</th>
              <th>Type</th>
          </tr>
          </thead>
          <tbody>
          <tr>
              <td>R_IELEMENT</td>
              <td>Rotation matrix I ELEMENT</td>
              <td>Py Numpy Array [N_DOFELEMET X N_DOFSELEMENT]</td>
          </tr>
          </tbody>
          </table>
        </dd>    
<d1>