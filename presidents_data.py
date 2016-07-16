from datetime import date


presidents_by_party = {
    "Independent": [
        {
            "name": "George Washington",
            "born": date(1732, 2, 22),
            "took_office": date(1789, 4, 30),
            "left_office": date(1797, 3, 4),
        }
    ],
    "Federalist": [
        {
            "name": "John Adams",
            "born": date(1735, 10, 30),
            "took_office": date(1797, 3, 4),
            "left_office": date(1801, 3, 4),
        }
    ],
    "Democratic-Republican": [
        {
            "name": "Thomas Jefferson",
            "born": date(1743, 4, 13),
            "took_office": date(1801, 3, 4),
            "left_office": date(1809, 3, 4),
        },
        {
            "name": "James Madison",
            "born": date(1751, 3, 16),
            "took_office": date(1809, 3, 4),
            "left_office": date(1817, 3, 4),
        },
        {
            "name": "James Monroe",
            "born": date(1758, 4, 28),
            "took_office": date(1817, 3, 4),
            "left_office": date(1825, 3, 4),
        },
        {
            "name": "John Quincy Adams",
            "born": date(1767, 7, 11),
            "took_office": date(1825, 3, 4),
            "left_office": date(1829, 3, 4),
        }
    ],
    "Democratic": [
        {
            "name": "Andrew Jackson",
            "born": date(1767, 3, 15),
            "took_office": date(1829, 3, 4),
            "left_office": date(1837, 3, 4),
        },
        {
            "name": "Martin Van Buren",
            "born": date(1782, 12, 5),
            "took_office": date(1837, 3, 4),
            "left_office": date(1841, 3, 4),
        },
        {
            "name": "James K. Polk",
            "born": date(1795, 11, 2),
            "took_office": date(1845, 3, 4),
            "left_office": date(1849, 3, 4),
        },
        {
            "name": "Franklin Pierce",
            "born": date(1804, 11, 23),
            "took_office": date(1853, 3, 4),
            "left_office": date(1857, 3, 4),
        },
        {
            "name": "James Buchanan",
            "born": date(1791, 4, 23),
            "took_office": date(1857, 3, 4),
            "left_office": date(1861, 3, 4),
        },
        {
            "name": "Andrew Johnson",
            "born": date(1808, 12, 29),
            "took_office": date(1865, 4, 15),
            "left_office": date(1869, 3, 4),
        },
        {
            "name": "Grover Cleveland",
            "born": date(1837, 3, 18),
            "took_office": date(1885, 3, 4),
            "left_office": date(1889, 3, 4),
        },
        {
            "name": "Grover Cleveland",
            "born": date(1837, 3, 18),
            "took_office": date(1893, 3, 4),
            "left_office": date(1897, 3, 4),
        },
        {
            "name": "Woodrow Wilson",
            "born": date(1856, 12, 28),
            "took_office": date(1913, 3, 4),
            "left_office": date(1921, 3, 4),
        },
        {
            "name": "Franklin D. Roosevelt",
            "born": date(1882, 1, 30),
            "took_office": date(1933, 3, 4),
            "left_office": date(1945, 4, 12),
        },
        {
            "name": "Harry S. Truman",
            "born": date(1884, 5, 8),
            "took_office": date(1945, 4, 12),
            "left_office": date(1953, 1, 20),
        },
        {
            "name": "John F. Kennedy",
            "born": date(1917, 5, 29),
            "took_office": date(1961, 1, 20),
            "left_office": date(1963, 11, 22),
        },
        {
            "name": "Lyndon B. Johnson",
            "born": date(1908, 8, 27),
            "took_office": date(1963, 11, 22),
            "left_office": date(1969, 1, 20),
        },
        {
            "name": "Jimmy Carter",
            "born": date(1924, 10, 1),
            "took_office": date(1977, 1, 20),
            "left_office": date(1981, 1, 20),
        },
        {
            "name": "Bill Clinton",
            "born": date(1946, 8, 19),
            "took_office": date(1993, 1, 20),
            "left_office": date(2001, 1, 20),
        },
        {
            "name": "Barack Obama",
            "born": date(1961, 8, 4),
            "took_office": date(2009, 1, 20),
            "left_office": date(2017, 1, 20),
        }
    ],
    "Whig": [
        {
            "name": "William Henry Harrison",
            "born": date(1773, 2, 9),
            "took_office": date(1841, 3, 4),
            "left_office": date(1841, 4, 4),
        },
        {
            "name": "John Tyler",
            "born": date(1790, 3, 29),
            "took_office": date(1841, 4, 4),
            "left_office": date(1845, 3, 4),
        },
        {
            "name": "Zachary Taylor",
            "born": date(1784, 11, 24),
            "took_office": date(1849, 3, 4),
            "left_office": date(1850, 7, 9),
        },
        {
            "name": "Millard Fillmore",
            "born": date(1800, 1, 7),
            "took_office": date(1850, 7, 9),
            "left_office": date(1853, 3, 4),
        }
    ],
    "Republican": [
        {
            "name": "Abraham Lincoln",
            "born": date(1809, 2, 12),
            "took_office": date(1861, 3, 4),
            "left_office": date(1865, 4, 15),
        },
        {
            "name": "Ulysses S. Grant",
            "born": date(1822, 4, 27),
            "took_office": date(1869, 3, 4),
            "left_office": date(1877, 3, 4),
        },
        {
            "name": "Rutherford B. Hayes",
            "born": date(1822, 10, 4),
            "took_office": date(1877, 3, 4),
            "left_office": date(1881, 3, 4),
        },
        {
            "name": "James A. Garfield",
            "born": date(1831, 11, 19),
            "took_office": date(1881, 3, 4),
            "left_office": date(1881, 9, 19),
        },
        {
            "name": "Chester A. Arthur",
            "born": date(1829, 10, 5),
            "took_office": date(1881, 9, 19),
            "left_office": date(1885, 3, 4),
        },
        {
            "name": "Benjamin Harrison",
            "born": date(1833, 8, 20),
            "took_office": date(1889, 3, 4),
            "left_office": date(1893, 3, 4),
        },
        {
            "name": "William McKinley",
            "born": date(1843, 1, 29),
            "took_office": date(1897, 3, 4),
            "left_office": date(1901, 9, 14),
        },
        {
            "name": "Theodore Roosevelt",
            "born": date(1858, 10, 27),
            "took_office": date(1901, 9, 14),
            "left_office": date(1909, 3, 4),
        },
        {
            "name": "William Howard Taft",
            "born": date(1857, 9, 15),
            "took_office": date(1909, 3, 4),
            "left_office": date(1913, 3, 4),
        },
        {
            "name": "Warren G. Harding",
            "born": date(1865, 11, 2),
            "took_office": date(1921, 3, 4),
            "left_office": date(1923, 8, 2),
        },
        {
            "name": "Calvin Coolidge",
            "born": date(1872, 7, 4),
            "took_office": date(1923, 8, 2),
            "left_office": date(1929, 3, 4),
        },
        {
            "name": "Herbert Hoover",
            "born": date(1874, 8, 10),
            "took_office": date(1929, 3, 4),
            "left_office": date(1933, 3, 4),
        },
        {
            "name": "Dwight D. Eisenhower",
            "born": date(1890, 10, 14),
            "took_office": date(1953, 1, 20),
            "left_office": date(1961, 1, 20),
        },
        {
            "name": "Richard Nixon",
            "born": date(1913, 1, 9),
            "took_office": date(1969, 1, 20),
            "left_office": date(1974, 8, 9),
        },
        {
            "name": "Gerald Ford",
            "born": date(1913, 7, 14),
            "took_office": date(1974, 8, 9),
            "left_office": date(1977, 1, 20),
        },
        {
            "name": "Ronald Reagan",
            "born": date(1911, 2, 6),
            "took_office": date(1981, 1, 20),
            "left_office": date(1989, 1, 20),
        },
        {
            "name": "George H. W. Bush",
            "born": date(1924, 6, 12),
            "took_office": date(1989, 1, 20),
            "left_office": date(1993, 1, 20),
        },
        {
            "name": "George W. Bush",
            "born": date(1946, 7, 6),
            "took_office": date(2001, 1, 20),
            "left_office": date(2009, 1, 20),
        }
    ]
}
