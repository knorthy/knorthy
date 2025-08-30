<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Tiffany Lyssa's Profile</title>
  <script src="https://cdn.jsdelivr.net/npm/react@18.2.0/umd/react.production.min.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/react-dom@18.2.0/umd/react-dom.production.min.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/babel-standalone@7.22.5/babel.min.js"></script>
  <script src="https://cdn.tailwindcss.com"></script>
</head>
<body class="bg-gray-900 text-white font-sans">
  <div id="root"></div>
  <script type="text/babel">
    function App() {
      return (
        <div className="max-w-4xl mx-auto p-6">
          {/* About Me */}
          <section className="mb-8">
            <h1 className="text-3xl font-bold mb-2">💫 About Me</h1>
            <p className="text-lg">Hi, I'm Tiffany Lyssa, a Computer Science student</p>
          </section>

          {/* Socials */}
          <section className="mb-8">
            <h2 className="text-2xl font-semibold mb-4">🌐 Socials</h2>
            <div className="flex flex-wrap gap-2">
              <a href="https://facebook.com/Tiffany Lyssa" target="_blank" rel="noopener noreferrer">
                <img src="https://img.shields.io/badge/Facebook-%231877F2.svg?logo=Facebook&logoColor=white" alt="Facebook" className="h-8" />
              </a>
              <a href="https://instagram.com/L.ystffny" target="_blank" rel="noopener noreferrer">
                <img src="https://img.shields.io/badge/Instagram-%23E4405F.svg?logo=Instagram&logoColor=white" alt="Instagram" className="h-8" />
              </a>
              <a href="https://linkedin.com/in/Tiffany Lyssa" target="_blank" rel="noopener noreferrer">
                <img src="https://img.shields.io/badge/LinkedIn-%230077B5.svg?logo=linkedin&logoColor=white" alt="LinkedIn" className="h-8" />
              </a>
              <a href="mailto:tiffanylyssa.p@gmail.com">
                <img src="https://img.shields.io/badge/Email-D14836?logo=gmail&logoColor=white" alt="Email" className="h-8" />
              </a>
            </div>
          </section>

          {/* Tech Stack */}
          <section className="mb-8">
            <h2 className="text-2xl font-semibold mb-4">💻 Tech Stack</h2>
            <div className="flex flex-wrap gap-2">
              <img src="https://img.shields.io/badge/c++-%2300599C.svg?style=for-the-badge&logo=c%2B%2B&logoColor=white" alt="C++" className="h-8" />
              <img src="https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54" alt="Python" className="h-8" />
              <img src="https://img.shields.io/badge/react_native-%2320232a.svg?style=for-the-badge&logo=react&logoColor=%2361DAFB" alt="React Native" className="h-8" />
              <img src="https://img.shields.io/badge/apache-%23D42029.svg?style=for-the-badge&logo=apache&logoColor=white" alt="Apache" className="h-8" />
              <img src="https://img.shields.io/badge/mysql-4479A1.svg?style=for-the-badge&logo=mysql&logoColor=white" alt="MySQL" className="h-8" />
              <img src="https://img.shields.io/badge/adobe-%23FF0000.svg?style=for-the-badge&logo=adobe&logoColor=white" alt="Adobe" className="h-8" />
              <img src="https://img.shields.io/badge/Adobe%20After%20Effects-9999FF.svg?style=for-the-badge&logo=Adobe%20After%20Effects&logoColor=white" alt="Adobe After Effects" className="h-8" />
              <img src="https://img.shields.io/badge/Adobe%20Premiere%20Pro-9999FF.svg?style=for-the-badge&logo=Adobe%20Premiere%20Pro&logoColor=white" alt="Adobe Premiere Pro" className="h-8" />
              <img src="https://img.shields.io/badge/figma-%23F24E1E.svg?style=for-the-badge&logo=figma&logoColor=white" alt="Figma" className="h-8" />
              <img src="https://img.shields.io/badge/Framer-black?style=for-the-badge&logo=framer&logoColor=blue" alt="Framer" className="h-8" />
              <img src="https://img.shields.io/badge/Canva-%2300C4CC.svg?style=for-the-badge&logo=Canva&logoColor=white" alt="Canva" className="h-8" />
              <img src="https://img.shields.io/badge/blender-%23F5792A.svg?style=for-the-badge&logo=blender&logoColor=white" alt="Blender" className="h-8" />
              <img src="https://img.shields.io/badge/adobe%20photoshop-%2331A8FF.svg?style=for-the-badge&logo=adobe%20photoshop&logoColor=white" alt="Adobe Photoshop" className="h-8" />
              <img src="https://img.shields.io/badge/SketchUp-005F9E?style=for-the-badge&logo=sketchup&logoColor=white" alt="SketchUp" className="h-8" />
              <img src="https://img.shields.io/badge/git-%23F05033.svg?style=for-the-badge&logo=git&logoColor=white" alt="Git" className="h-8" />
              <img src="https://img.shields.io/badge/-Arduino-00979D?style=for-the-badge&logo=Arduino&logoColor=white" alt="Arduino" className="h-8" />
              <img src="https://img.shields.io/badge/unity-%23000000.svg?style=for-the-badge&logo=unity&logoColor=white" alt="Unity" className="h-8" />
            </div>
          </section>

          {/* GitHub Stats */}
          <section className="mb-8">
            <h2 className="text-2xl font-semibold mb-4">📊 GitHub Stats</h2>
            <div className="flex flex-col gap-4 items-center">
              <img
                src="https://nirzak-streak-stats.vercel.app/?user=knorthy&theme=dark&hide_border=false"
                alt="GitHub Streak Stats"
                className="w-[500px] h-auto"
              />
              <img
                src="https://github-readme-stats.vercel.app/api/top-langs/?username=knorthy&theme=dark&hide_border=false&include_all_commits=false&count_private=false&layout=compact"
                alt="GitHub Top Languages"
                className="w-[500px] h-auto"
              />
            </div>
          </section>

          {/* Visit Counter */}
          <section className="text-center">
            <a href="https://visitcount.itsvg.in" target="_blank" rel="noopener noreferrer">
              <img src="https://visitcount.itsvg.in/api?id=knorthy&icon=0&color=0" alt="Visit Counter" className="h-8" />
            </a>
          </section>
        </div>
      );
    }

    ReactDOM.render(<App />, document.getElementById('root'));
  </script>
</body>
</html>
