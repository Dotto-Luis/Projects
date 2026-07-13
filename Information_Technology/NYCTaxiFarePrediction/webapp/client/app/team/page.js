import React from 'react';
import TeamMember from '../ui/TeamMember';

const TeamPage = () => {
  const teamMembers = [
    {
      name: 'Cristian Horacio Belussi',
      profilePicture: '20509133?v=4',
      githubUsername: 'xtianhb',
      linkedinUsername: 'xtianhb',
    },
    {
      name: 'Jorge Damian Bringas',
      profilePicture: '140633379?v=4',
      githubUsername: 'xtianhb',
      linkedinUsername: 'jorge-damián-bringas-296b92271',
    },
    {
      name: 'Jose David Nuñez',
      profilePicture: '78088827?v=4',
      githubUsername: 'josedavidnup',
      linkedinUsername: 'josedavidnpx',
    },
    {
      name: 'Luis Dotto',
      profilePicture: '93018629?v=4',
      githubUsername: 'Dotto-Luis',
      linkedinUsername: 'luisdotto',
    },
    {
      name: 'Sergio Buzzi',
      profilePicture: '12287751?v=4',
      githubUsername: 'sergiobuzzi',
      linkedinUsername: 'sergio-martin-buzzi-data-scientist',
    },
  ];

  return (
    <div className='container mx-auto p-4'>
      <h1 className='text-3xl font-bold mb-4 text-center'>Our Team</h1>
      <div className='grid grid-cols-1 sm:grid-cols-2 md:grid-cols-2 lg:grid-cols-3 gap-4'>
        {teamMembers.map((member, index) => (
          <TeamMember key={index} {...member} />
        ))}
      </div>
    </div>
  );
};

export default TeamPage;
